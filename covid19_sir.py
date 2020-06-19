# Alec Barker
# covid19-sir.py
"""
Gets data from the covid19-condensed-data file, graphs it, and creates an SIR
model to match it.
"""

import datetime as dt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


"""
Gets the number of infected individuals each day from the
covid19-condensed-data file.
"""

f = open("Data Files/covid19_condensed_data", "rt")

dates = []
dailyInfected = []

for i, line in enumerate(f):
    data = line.split(",")
    date = data[0]
    
    # Ignore first 13 days where the numbers varied but were largely 0,
    # likely do to not reporting cases to official health organizations
    if i >= 13:
        numInfected = data[1]
        
        if numInfected.endswith("\n"):
            numInfected = numInfected[:-1]
        
        dates.append(date)
        dailyInfected.append(int(numInfected))
        
f.close()

# The dates from the start of the pandemic until May 6, 2020 that will display
# on the x axis
x = [dt.datetime.strptime(d, "%Y/%m/%d").date() for d in dates]



"""
Sets up the SIR model.
"""
# Initial values
S0 = 7722935549
I0 = 1
R0 = 0
N = S0 + I0 + R0
r0 = 3.09
duration = 14
gamma = 1 / duration
beta = r0 / duration

# Initially set to a large number then reduced based on the output of the
# print statement about length of the pandemic
numDays = 535

def sir(init, t):
    S, I, R = init
    dSdt = -1 * beta * I * S/N
    dIdt = beta * I * S/N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

init = S0, I0, R0

tpoints = range(numDays)

initpoints = odeint(sir, init, tpoints)
spoints, ipoints, rpoints = initpoints.T

# The dates from the start of the pandemic until June 30, 2021 that will
# display on the x axis
x2 = [x[0] + dt.timedelta(days=i) for i in range(numDays)]



"""
Graphs data.
"""
# Current situation with real and SIR data
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.plot(x, dailyInfected, linewidth=2)
plt.gcf().autofmt_xdate()
plt.title("Daily Confirmed Cases", fontsize="xx-large")
plt.xlabel("Date", size="x-large")
plt.ylabel("Population", size="x-large")
plt.show()

# Current situation with real and SIR data (zoomed on real)
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.gca().set_ylim([0, 180000])
plt.plot(x, dailyInfected, label="Real Data", linewidth=2)
plt.plot(x, ipoints[:len(x)], c="r", alpha=0.5, label="SIR Model Data", linewidth=2)
plt.gcf().autofmt_xdate()
plt.legend(prop={'size': 15})
plt.title("Daily Confirmed Cases", fontsize="xx-large")
plt.xlabel("Date", size="x-large")
plt.ylabel("Population", size="x-large")
plt.show()

# Current situation with real and SIR data (zoomed out to SIR)
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.plot(x, dailyInfected, label="Real Data", linewidth=2)
plt.plot(x, ipoints[:len(x)], c="r", alpha=0.5, label="SIR Model Data", linewidth=2)
plt.gcf().autofmt_xdate()
plt.legend(prop={'size': 15})
plt.title("Daily Confirmed Cases", fontsize="xx-large")
plt.xlabel("Date", size="x-large")
plt.ylabel("Population (Billions)", size="x-large")
plt.show()

# SIR of entire outbreak timeline
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=40))
plt.plot(x2, spoints, c="b", alpha=0.5, label="Susceptible", linewidth=2)
plt.plot(x2, ipoints, c="r", alpha=0.5, label="Infected", linewidth=2)
plt.plot(x2, rpoints, c="g", alpha=0.5, label="Recovered", linewidth=2)
plt.axvline(x=x2[len(x) - 1], c="k", label="June 19, 2020", linewidth=2)
plt.gcf().autofmt_xdate()
plt.legend(prop={'size': 12})
plt.title("SIR Model Daily Values", fontsize="xx-large")
plt.xlabel("Date", size="x-large")
plt.ylabel("Population (Billions)", size="x-large")
plt.show()



"""
Gets statistics about graphs.
"""
print("Current number of infected individuals:",
      dailyInfected[len(x) - 1])
print("Current number of infected individuals using SIR:",
      ipoints[len(x) - 1])

for i, dailyValue in enumerate(ipoints):
    if dailyValue < 1:
        print("Using SIR, the infection is expected to die out after {} days on {}" \
              .format(i, x2[i]))
        print("Using SIR, the total number of infected/recovered is:",
              rpoints[i])
        print("Using SIR, the total number of uninfected is:", spoints[i])
        break
    
print("Using SIR, the peak number of individuals infected in a single day is {} on {}" \
      .format(max(ipoints), x2[np.argmax(ipoints)]))