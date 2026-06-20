## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums

import DomesticAdvisorTable
import BaseAdvisorWindow

## Based on work from R&R, Robert Surcouf, Domestic Advisor Screen
## WTP, KMH, Domestic Advisor import/export toggle - shows the same import/export state as ImportExportAdvisor,
## but with the actual threshold numbers, and lets the player click a cell to cycle CvCity::togleTrade()'s presets
## directly from this table instead of opening the per-city import/export popup.

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class ImportExportExtAdvisor(BaseAdvisorWindow.BaseAdvisorWindow):
	def __init__(self, parent):
		BaseAdvisorWindow.BaseAdvisorWindow.__init__(self, parent, "ImportExportExtStateClass")

	def drawColonyRowCustom(self, iCity, pCity):
		self.tableManager.addInt("<color=255,255,0>Toggle</color>", iCity, -1, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)

	def drawColonyCell(self, iCity, pCity, iYield, pYieldInfo):
		bExportYield = pCity.isExport(iYield)
		bImportYield = pCity.isImport(iYield)
		importAmount = pCity.getImportsLimit(iYield)
		exportAmount = pCity.getMaintainLevel(iYield)
		if (bExportYield and bImportYield):
			self.tableManager.addInt("<color=255,255,0>" + str(importAmount/100) + u"/" + str(exportAmount/100) + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		elif (not bExportYield and bImportYield):
			self.tableManager.addInt("<color=0,255,0>" + str(importAmount/100) + u"/-" + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		elif (bExportYield and not bImportYield):
			self.tableManager.addInt("<color=255,0,0>" + u"-/" + str(exportAmount/100) + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)
		else:
			self.tableManager.addInt("<color=255,255,255>" + u"-/-" + u"</color>", iCity, iYield, WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT)

	def createTableHeader(self):
		# create table headers
		self.tableManager.addHeaderButton()
		self.tableManager.addHeaderCityName()
		self.tableManager.addHeaderTxt("Domestic", 100)
		self.tableManager.addHeaderArrayYields()

	def handleInput(self, inputClass):
		if (inputClass.getNotifyCode() == NotifyCode.NOTIFY_LISTBOX_ITEM_SELECTED and inputClass.getButtonType() == WidgetTypes.WIDGET_CONDENSED_YIELD_IMPORT_EXPORT and inputClass.getData1() < len(self.parent.Cities)):
			pCity = self.parent.Cities[inputClass.getData1()]
			iYield = inputClass.getData2()

			if (iYield >= 0):
				pCity.togleTrade(pCity.getID(), iYield)
			else:
				pCity.togleDomestigTrade()
			return 0

		return -1
