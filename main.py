from utils import *
from covid import *

globalConfirmed = loadAndCleanData("confirmedGlobal.csv")
confirmed = correctDateFormatConfirmed(globalConfirmed)
#print(confirmed)

globalDeaths = loadAndCleanData("deathsGlobal.csv")
deaths = correctDateFormatDeaths(globalDeaths)

globalRecovered = loadAndCleanData("recoveredGlobal.csv")
recovered = correctDateFormatRecovered(globalRecovered)

globalData = mergeData(confirmed, recovered, "Recovered")
globalData = mergeData(globalData, deaths, "Deaths")

#plotTimeline(globalData, "Date", "Confirmed")
#plotTimeline(globalData, "Date", "Recovered")
#plotTimeline(globalData, "Date", "Deaths")

#plotMultipleTimelines(globalData, "Date", "Recovered", "Deaths")
#plotMultipleTimelines(globalData, "Date", "Confirmed", "Deaths")
#plotMultipleTimelines(globalData, "Date", "Confirmed", "Recovered")

topCorrelations(globalData, "", 5)
