# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    Date = []
    Months = 0
    dictionary = []
    Total = []
    Average = []
    first_row = 0
    highest_profit = []
    change = 0
    next_row = 0
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    
    csv_header = next(csvreader)

    # Read each row of data after the header
    
    
    for row in csvreader:
        
        
        # count the total months and add it to the counter
             Months +=  1
        
        # convert profit column into an integer list
             Total.append(int(row[1]))
            
             Date.append(row[0])

        
             first_row = row[1] 

             change = (int(first_row)) - (int(next_row))
             Average.append(change)

             next_row = row[1]


        

    # create dicitionary to find date of largest profit and largest loss date. 
    # the date should correlate to the largest changes in the Average list

    dictionary = dict(zip(Date, Total))
    highest_profit = max(dictionary, key= dictionary.get) 
    largest_loss = min(dictionary, key= dictionary.get)

    #remove first change between zero and first value. not a great way to do it but it worked for me.

    del Average[0]



      
    average_change = sum(Average)/ len(Average)

    
    #find max change and min change in Average list. which is a list of the changes calculated

    high = max(Average)
    low = min(Average)
    Total = sum(Total)
    
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {Months}")
    print(f"Total Profit/Loss: : ${Total}")
    print(f'Average Change: ${average_change}')
    print(f"Largest loss: {largest_loss} ${low}")  
    print(f"Highest Profit: {highest_profit} ${high}")

output_path = os.path.join("budget_results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:

    # Initialize csv.writer
    writer = csv.writer(text_file, delimiter=',')
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------"])
    writer.writerow([f"Total Months: {Months}"])
    writer.writerow([f"Total Profit/Loss: : ${Total}"])
    writer.writerow([f'Average Change: ${average_change}'])
    writer.writerow([f"Largest loss: {largest_loss} ${low}"])
    writer.writerow([f"Highest Profit: {highest_profit} ${high}"])
