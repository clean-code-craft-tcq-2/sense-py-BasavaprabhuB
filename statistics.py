import math 

class EmailAlert():
  def __init__(self):
    self.emailSent = False


class LEDAlert():
    def __init__(self):
        self.ledGlows =  False


class StatsAlerter():
    def __init__(self, maxThreshold, alerts) :
        self.maxThreshold = maxThreshold
        self.alerts = alerts

    def checkAndAlert(self, numbers):
        computedStats = calculateStats(numbers)

        if computedStats["max"] > self.maxThreshold:
            self.alerts[0].emailSent = True
            self.alerts[1].ledGlows = True


def calculateStats(numbers):
  # Dictionary declaration
  computedStats = {}
  # if no numbers are given
  if not numbers:
    computedStats={"max": math.nan, "min": math.nan, "avg": math.nan}
  else:
    #minimum of numbers
    computedStats["min"] = min(numbers)

    #maximum of numbers
    computedStats["max"] = max(numbers)

    #average of numbers
    computedStats["avg"] = sum(numbers)/len(numbers)
    return computedStats
