#Steve Bennett - Week 3 Assigment
#Python Election Assigment
import csv
import os

#CSV file containing our data
file = os.path.join('Resources', 'election_data.csv')

candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"] #clean list for ouput
totalvotes = 0              #ensures we have clean start of no votes
percent_name = [0,0,0]      #sets list size and values to zero
percent_val = [0,0,0]       #sets list size and values to zero

with open(file, 'r') as csvfile:
    votes = csv.reader(csvfile, delimiter=',')
    
    next(votes, None)       #skips the header
    
    for row in votes:       #primary loop counting total votes + individual candidate votes
        totalvotes += 1
        if row[2] == candidate[0]:
            percent_name[0] = percent_name[0] + 1
        elif row[2] == candidate[1]:
            percent_name[1] = percent_name[1] + 1
        elif row[2] == candidate[2]:
            percent_name[2] = percent_name[2] + 1

#if charles > diana and charles > raymon
if percent_name[0] > percent_name[1] and percent_name[0] > percent_name[2]:
    winner = candidate[0]
#if diana > charles and diana > raymon
elif percent_name[1] > percent_name[0] and percent_name[1] > percent_name[2]:
    winner = candidate[1]
#raymon is default the last option
else:
    winner = candidate[2]

#calculates the percentage of votes + formats into ##.###% value
for i in range(3):
    percent_val[i] = '{:.3f}'.format((percent_name[i] / totalvotes)*100)

#on screen output
print('Election Results')
print('-----------------------------------------------------')
print(f'Total Votes: {totalvotes}')
print('-----------------------------------------------------')
print(f'{candidate[0]}: {percent_val[0]}% ({percent_name[0]})')
print(f'{candidate[1]}: {percent_val[1]}% ({percent_name[1]})')
print(f'{candidate[2]}: {percent_val[2]}% ({percent_name[2]})')
print('-----------------------------------------------------')
print(f'Winner: {winner}')
print('-----------------------------------------------------')

#I will also output the same details to a text file:
outputpath = os.path.join('analysis', 'output.txt')
with open(outputpath, 'w') as f:
    f.write('Election Results\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Total Votes: {totalvotes}\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'{candidate[0]}: {percent_val[0]}% ({percent_name[0]})\n')
    f.write(f'{candidate[1]}: {percent_val[1]}% ({percent_name[1]})\n')
    f.write(f'{candidate[2]}: {percent_val[2]}% ({percent_name[2]})\n')
    f.write('-----------------------------------------------------\n')
    f.write(f'Winner: {winner}\n')
    f.write('-----------------------------------------------------')