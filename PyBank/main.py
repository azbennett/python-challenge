#Steve Bennett - Week 3 Assigment
#Python Bank Assigment
import csv
import os
import sys

#CSV file containing our data
file = os.path.join('Resources', 'budget_data.csv')

greatestinc = 0     #tracker for greatest increase in profits
greatestdec = 0     #tracker for greatest decrease in profits
total = 0           #tracker for total profits
months = 0          #tracker for total months
average = 0         #tracker for average change 
skipfirst = 1       #lets me enter my first loop
totalmo = 0         #used for calculating average
difference = []     #list for storing the difference values as we go through the loops
old = 0             #used for old value and new value for change/difference
new = 0             #used for old value and new value for change/difference
diff = 0            #used for old value and new value for change/difference

with open(file, 'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    
    next(budget, None) #skips headers

    #primary loop adding up total months, total value, difference/change, and greatest inc/dec
    for row in budget: 
        total = total + int(row[1])
        months = months + 1
        
        #first loop stores the first value as old, but does not calculate differences since we have no old value to compare to
        if skipfirst == 1: 
            old = int(row[1])
            skipfirst = 0
        #all other loops we store  new vs old for change/difference
        else:
            new = int(row[1])
            diff = new - old
            difference.append(diff)
            old = int(row[1])
        #check for  greatest inc / dec
        if  diff > greatestinc:
            greatestinc = diff
            greatestincdate = row[0]
        if  diff < greatestdec:
            greatestdec = diff
            greatestdecdate = row[0]

    #calculates the average change values
    for i in difference:
        totalmo = totalmo + i
    average = round(totalmo / len(difference), 2)

#on screen output
print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {greatestincdate} (${greatestinc})')
print(f'Greatest Decrease in Profits: {greatestdecdate} (${greatestdec})')

#I will also output the same details to a text file:
outputpath = os.path.join('analysis', 'output.txt')
with open(outputpath, 'w') as f:
    f.write('Financial Analysis\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Months: {months}\n')
    f.write(f'Total: ${total}\n')
    f.write(f'Average Change: ${average}\n')
    f.write(f'Greatest Increase in Profits: {greatestincdate} (${greatestinc})\n')
    f.write(f'Greatest Decrease in Profits: {greatestdecdate} (${greatestdec})')