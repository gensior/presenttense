from mx.DateTime import DateTime, DateTimeDeltaFromSeconds, now

present = now()
historystart = DateTime(-10000, 1, 1)

def historical(historyend=DateTime(present.year, 12, 31, 23, 59, 59)):
	return (historyend - historystart).seconds

def yearical(yearend=DateTime(present.year, 12, 31, 23, 59, 59)):
	yearstart = DateTime(present.year, 1, 1)
	return (yearend - yearstart).seconds

def yearify(historydate):
	historyscale = historical()
	historypoint = historical(historyend=historydate)
	historyratio = (historyscale - historypoint)/historyscale
	yearscale = yearical()
	yearpoint = DateTimeDeltaFromSeconds(yearscale * historyratio)
	return DateTime(present.year, 12, 31, 23, 59, 59) - yearpoint

def historify(yeardate):
	yearscale = yearical()
	yearpoint = yearical(yearend=yeardate)
	yearratio = (yearscale - yearpoint)/yearscale
	historyscale = historical()
	historypoint = DateTimeDeltaFromSeconds(historyscale * yearratio)
	return DateTime(present.year, 12, 31, 23, 59, 59) - historypoint

def epoch_to_historical(seconds):
    diff = DateTimeDeltaFromSeconds(seconds)
    return historystart + diff

def epoch_to_yearical(seconds):
    return yearify(epoch_to_historical(seconds))