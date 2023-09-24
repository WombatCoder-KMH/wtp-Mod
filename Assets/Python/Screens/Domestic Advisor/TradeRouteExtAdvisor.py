## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

import DomesticAdvisorTable
import BaseAdvisorWindow

## Based on work from R&R, Robert Surcouf,  Domestic Advisor Screen

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class TradeRouteExtAdvisor(BaseAdvisorWindow.BaseAdvisorWindow):
	def __init__(self, parent):
		BaseAdvisorWindow.BaseAdvisorWindow.__init__(self, parent, "TradeRouteExtStateClass")

	def drawTableContent(self):
		player = gc.getPlayer(gc.getGame().getActivePlayer())

		self.numUnits = 0

		(unit, iter) = player.firstUnit()
		while (unit):
			if (not unit.isCargo() and not unit.isDelayedDeath() and unit.cargoSpace() > 0):
#			if (not unit.isCargo() and not unit.isDelayedDeath() and unit.canAssignTradeRoute(-1, False)):
				self.numUnits = self.numUnits + 1
			(unit, iter) = player.nextUnit(iter)

		self.tableManager.setNumRows(self.numUnits)

		(unit, iter) = player.firstUnit()
		while (unit):
			if (not unit.isCargo() and not unit.isDelayedDeath() and unit.cargoSpace() > 0):
				self.drawTradeUnitLine(unit)
			(unit, iter) = player.nextUnit(iter)
	
	def drawTradeUnitLine(self, unit):
#		CvUtil.pyPrint("unit.getID() " + str(unit.getID()))

		automationType = unit.getGroup().getAutomateType()
		fullAutoTrade = automationType == 7
		routeAutoTrade = automationType == 6

		self.tableManager.addPanelButton(unit.getButton(), WidgetTypes.WIDGET_GENERAL, unit.getID(), -2) # -2 is a hack to distinguis from other events.

		if (fullAutoTrade):
			self.tableManager.addText("<color=255,0,0>" + unit.getName() + u"</color>", unit.getID(), -1, WidgetTypes.WIDGET_UNIT_MODEL)
		elif(routeAutoTrade):
			self.tableManager.addText("<color=255,255,0>" + unit.getName() + u"</color>", unit.getID(), -1, WidgetTypes.WIDGET_UNIT_MODEL)
		else:
			self.tableManager.addText("<color=0,255,0>" + unit.getName() + u"</color>", unit.getID(), -1, WidgetTypes.WIDGET_UNIT_MODEL)

		self.tableManager.addInt(unit.getID(), unit.getID(), -1, WidgetTypes.WIDGET_UNIT_MODEL)

		self.tableManager.addText("AutomateType " + str(unit.getGroup().getAutomateType()), unit.getID(), -1, WidgetTypes.WIDGET_UNIT_MODEL)

	def setDirty(self):
		self.dirty = True

	def createTableHeader(self):
		self.tableManager.addHeaderButton()
		self.tableManager.addHeaderTxt("Unit name", 400)
		self.tableManager.addHeaderTxt("Unit id", 100)
		self.tableManager.addHeaderTxt("Debug Info", 400)

	def handleInput (self, inputClass):
#		CvUtil.pyPrint("inputClass.getNotifyCode() " + str(inputClass.getNotifyCode()))
#		CvUtil.pyPrint("inputClass.getButtonType() " + str(inputClass.getButtonType()))
#		CvUtil.pyPrint("inputClass.getData1() " + str(inputClass.getData1()))
#		CvUtil.pyPrint("inputClass.getData2() " + str(inputClass.getData2()))

		if (inputClass.getNotifyCode() == 0 and inputClass.getButtonType() == 24):
			if (inputClass.getData2() == -2):
				return self.handleUnitSelect(inputClass.getData1())
				
		if (inputClass.getNotifyCode() == 11 and inputClass.getButtonType() == 45):
			return self.handleUnitSelect(inputClass.getData1())

		return -1
	
	def handleUnitSelect(self, unitId):
#		CvUtil.pyPrint("unitId " + str(unitId))

		if (unitId >= 0):
			player = gc.getPlayer(gc.getGame().getActivePlayer())
			unit = player.getUnit(unitId)
			unit.select(True, False, False)
			return 0
		return -1
	