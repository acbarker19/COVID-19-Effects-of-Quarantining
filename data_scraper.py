# Alec Barker
# data-scraper.py
"""
Gets data from the covid19-data file and formats it by adding totals for each
day.
"""

dateData = {}

fileIn = open("Data Files/covid19_data", "rt")

for i, line in enumerate(fileIn):
    if i != 0:
        data = line.split(",")
        year = data[3]
        month = data[2]
        day = data[1]
        
        # To correctly sort by date, months or days with single digits must
        # have a 0 beforehand
        if len(month) == 1:
            month = "0{}".format(month)       
        if len(day) == 1:
            day = "0{}".format(day)
        
        date = "{}/{}/{}".format(year, month, day)
        numInfected = int(data[4])
        
        # If the date is not in the dictionary, create a new dictionary entry
        # with the number of infected individuals. Otherwise, add the number
        # of infected individuals to the existing number.
        if date in dateData:
            dateData[date] += numInfected
        else:
            dateData[date] = numInfected

fileIn.close()

# Sort the dates so they are in order
dateDataKeys = sorted(dateData)

fileOut = open("Data Files/covid19_condensed_data", "wt")

for i, key in enumerate(dateDataKeys):
    fileOut.write("{},{}".format(key, dateData[key]))
    
    # Adds a line break if the current value is not the last dictionary value
    if i != len(dateDataKeys) - 1:
        fileOut.write("\n")

fileOut.close()