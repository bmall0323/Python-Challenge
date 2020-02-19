# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

file_to_load = os.path.join("C:\\Test\\budget_data.csv")
file_to_output = os.path.join('output.csv')

#placeholders for re-formatted contents
total_months = 0
months = []
total_profit=0
revenue_change = []
revenue =[]

with open(file_to_load,newline='') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#   Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#    Read each row of data after the header
    for row in csvreader:
#    print(row)
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        revenue.append(int(row[1]))
        months.append(row[0])

    for x in range(1,len(revenue)):
        revenue_change.append (revenue[x] - revenue[x-1])
        average_change = sum(revenue_change) / len(revenue_change)
        max_change = max(revenue_change)
        min_change = min(revenue_change)
        max_date = months[(revenue_change.index(max_change))]
        min_date = months[(revenue_change.index(min_change))]
        
    line1 = ("Total months:  " + str(total_months))
    line2 = ("Total Profits/Losses:  $" + str(total_profit))
    line3 = ("Average Change:  $" + str(round(average_change,2)))
    line4 = ("Greatest Increase in Profits:  " + str(max_date) + "  ($" + str(max_change) + ")")
    line5 = ("Greatest Decrease in Profits:  " + str(min_date) + "  ($" + str(min_change) + ")")
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    
    with open(file_to_output, 'w', newline='') as output_file:

    # Initialize csv.writer
        csvwriter = csv.writer(output_file, delimiter=',')

        csvwriter.writerow([str(line1)])
        csvwriter.writerow([str(line2)])
        csvwriter.writerow([str(line3)])
        csvwriter.writerow([str(line4)])
        csvwriter.writerow([str(line5)])