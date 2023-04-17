#Steve Bennett - Week 3 Assigment
#Python Bank Assigment
import csv
import os
import statistics

#CSV file containing our data
file = os.path.join('Resources', 'budget_data.csv')

greatestinc = 0         #tracker for greatest increase in profits
greatestdec = 0         #tracker for greatest decrease in profits
totalprofitlosses = 0   #tracker for total profits
month_counter = 0       #tracker for total months
average = 0             #tracker for average change 
skipfirst = 1           #lets me enter my first loop to store previousval
totaldifferences = 0    #used for calculating average
difference = []         #list for storing the difference values as we go through the loops
previousval = 0         #used for old value and new value for change/difference
currentval = 0          #used for old value and new value for change/difference
changeval = 0           #used for old value and new value for change/difference

with open(file, 'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    
    next(budget, None) #skips headers

    #primary loop adding up total months, total value, difference/change, and greatest inc/dec
    for row in budget: 
        totalprofitlosses = totalprofitlosses + int(row[1])
        month_counter = month_counter + 1
        
        #first loop stores the first value as old, but does not calculate differences since we have no old value to compare to
        if skipfirst == 1: 
            previousval = int(row[1])
            skipfirst = 0
        #all other loops we store  new vs old for change/difference
        else:
            currentval = int(row[1])
            changeval = currentval - previousval
            difference.append(changeval)
            previousval = int(row[1])
        #check for  greatest inc / dec
        if  changeval > greatestinc:
            greatestinc = changeval
            greatestincdate = row[0]
        if  changeval < greatestdec:
            greatestdec = changeval
            greatestdecdate = row[0]

    #calculates the average change values
    for i in difference:
        totaldifferences = totaldifferences + i
    average = round(statistics.mean(difference),2) #total of difference[] list divided by 85 (length of the list)

#on screen output
print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {month_counter}')
print(f'Total: ${totalprofitlosses}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {greatestincdate} (${greatestinc})')
print(f'Greatest Decrease in Profits: {greatestdecdate} (${greatestdec})')

#I will also output the same details to a text file:
outputpath = os.path.join('analysis', 'output.txt')
with open(outputpath, 'w') as f:
    f.write('Financial Analysis\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Months: {month_counter}\n')
    f.write(f'Total: ${totalprofitlosses}\n')
    f.write(f'Average Change: ${average}\n')
    f.write(f'Greatest Increase in Profits: {greatestincdate} (${greatestinc})\n')
    f.write(f'Greatest Decrease in Profits: {greatestdecdate} (${greatestdec})')