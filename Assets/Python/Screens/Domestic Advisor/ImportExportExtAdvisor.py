## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import time
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

class ImportExportExtAdvisor(BaseAdvisorWindow.BaseAdvisorWindow):
	def __init__(self, parent):
		BaseAdvisorWindow.BaseAdvisorWindow.__init__(self, parent, "ImportExportExtStateClass")

	def drawColonyRowCustom(self, iCity, pCity):
		self.tableManager.addInt("<color=255,255,0>Toggle</color>", iCity, -1, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		return

	def drawColonyCell(self, iCity, pCity, iYield, pYieldInfo):
		bExportYield = pCity.isExport(iYield)
		bImportYield = pCity.isImport(iYield)
		importAmount = pCity.getImportsLimit(iYield)
		exportAmount = pCity.getMaintainLevel(iYield)
		## R&R, Robert Surcouf,  Domestic Advisor Screen - End
		if (bExportYield and bImportYield):
			self.tableManager.addInt("<color=255,255,0>" + str(importAmount/100) + u"/" + str(exportAmount/100) + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		elif (not bExportYield and bImportYield):
			self.tableManager.addInt("<color=0,255,0>" + str(importAmount/100) + u"/-" + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		elif (bExportYield and not bImportYield):
			self.tableManager.addInt("<color=255,0,0>" + u"-/" + str(exportAmount/100) + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		else:
			self.tableManager.addInt("<color=255,255,255>" + u"-/-" + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
#			self.tableManager.addPanelButton(ArtFileMgr.getInterfaceArtInfo("INTERFACE_BUTTONS_CITYSELECTION").getPath(), WidgetTypes.WIDGET_GENERAL, iCity, iYield)
#			self.tableManager.skipCell()

	def createTableHeader(self):
		# create table headers
		self.tableManager.addHeaderButton()
		self.tableManager.addHeaderCityName()
		self.tableManager.addHeaderTxt("Domestic", 100)
		self.tableManager.addHeaderArrayYields()


	def handleInput (self, inputClass):
#		CvUtil.pyPrint("inputClass.getNotifyCode() " + str(inputClass.getNotifyCode()))
#		CvUtil.pyPrint("inputClass.getButtonType() " + str(inputClass.getButtonType()))
#		CvUtil.pyPrint("inputClass.getData1() " + str(inputClass.getData1()))
#		CvUtil.pyPrint("inputClass.getData2() " + str(inputClass.getData2()))

#		CvUtil.pyPrint("dir(NotifyCode) " + str(dir(NotifyCode)))
#		CvUtil.pyPrint("dir(NotifyCode) " + ' '.join(list(NotifyCode)))
#		CvUtil.pyPrint("NotifyCode.NOTIFY_CLICKED " + str(int(NotifyCode.NOTIFY_CLICKED))) # 0
#		CvUtil.pyPrint("NotifyCode.NOTIFY_CURSOR_MOVE_ON " + str(int(NotifyCode.NOTIFY_CURSOR_MOVE_ON))) # 4
#		CvUtil.pyPrint("NotifyCode.NOTIFY_CURSOR_MOVE_OFF " + str(int(NotifyCode.NOTIFY_CURSOR_MOVE_OFF))) # 5
#		CvUtil.pyPrint("NotifyCode.NOTIFY_CHARACTER " + str(int(NotifyCode.NOTIFY_CHARACTER))) # 6
#		CvUtil.pyPrint("NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED " + str(int(NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED))) # 11
#		CvUtil.pyPrint("dir(WidgetTypes) " + str(dir(WidgetTypes)))

#		message = "Data1: " + str(inputClass.getData1()) + " Data2: " + str(inputClass.getData2()) + " NotifyCode: " + str(inputClass.getNotifyCode()) + " ButtonType: " + str(inputClass.getButtonType())
#		CyInterface().addImmediateMessage(message,"")
#		CvUtil.pyPrint(message)
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED and inputClass.getButtonType() == WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT and inputClass.getData1() < len(self.parent.Cities)):
#			CvUtil.pyPrint("handleInput start: " + str(time.clock()))
#			message = "Data1: " + str(inputClass.getData1()) + " Data2: " + str(inputClass.getData2()) + " Cities len: " + str(len(self.parent.Cities))
#			message = "City " + pCity.getName() + " " + str(pCity.getImportsLimit(iYield)) + " " + str(pCity.getMaintainLevel(iYield))
#			CyInterface().addImmediateMessage(message,"")
#			CvUtil.pyPrint(message)

#			pCity = gc.getCyActivePlayer().getCity(inputClass.getData1())
			pCity = self.parent.Cities[inputClass.getData1()] # gc.getCity(inputClass.getData1())
			iYield = inputClass.getData2()
#			CvUtil.pyPrint("dir(pCity) " + str(dir(pCity)))

#			pCity.setImportsLimit(iYield, 400)

			if (iYield >= 0):
				pCity.togleTrade(pCity.getID(), iYield)

#				CvUtil.pyPrint("handleInput end: " + str(time.clock()))
				return 0
			else:
				pCity.togleDomestigTrade()
#				CvUtil.pyPrint("handleInput end: " + str(time.clock()))
				return 0

#			if (inputClass.getButtonType() == WidgetTypes.WIDGET_GENERAL and inputClass.getData1() < len(self.parent.Cities)):
#				pCity = gc.getCyActivePlayer().getCity(inputClass.getData1())
#				pCity = self.parent.Cities[inputClass.getData1()] # gc.getCity(inputClass.getData1())
#				iYield = inputClass.getData2()

#				message = "Data1: " + str(inputClass.getData1()) + " Data2: " + str(inputClass.getData2()) + " Cities len: " + str(len(self.parent.Cities))
#				message = "City " + pCity.getName() + " " + str(pCity.getImportsLimit(iYield)) + " " + str(pCity.getMaintainLevel(iYield))

#				CyInterface().addImmediateMessage(message,"")
#				CvUtil.pyPrint(message)

#				pCity.setImportsLimit(iYield, 400)
#				return 0

#		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED):
#			if (inputClass.getButtonType() == self.WIDGET_JUMP_TO_SETTLEMENT_BUTTON or inputClass.getButtonType() == WidgetTypes.WIDGET_JUMP_TO_SETTLEMENT):
#				self.parent.getScreen().hideScreen()
#				CyCamera().JustLookAtPlot(gc.getMap().plotByIndex(inputClass.getData1()))
#				return 0
		
		return -1