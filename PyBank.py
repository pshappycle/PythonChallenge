#import modules
import csv
import os

#Variables
row_count = 0
months =[]
net_total = 0
pl =[]
profit_increase = 0
profit_increase_month = 0
profit_decrease = 0
profit_decrease_month = 0

with open("PYBank.csv") as csvfile:
    
    #csv reader
    csvreader = csv.reader(csvfile)
    
    #set my header row
    header = next(csvreader)

    #set my first row of values
    prev_row = next(csvreader)
    months.append(prev_row[0])

    net_total = int(prev_row[1])

    profit_increase = int(prev_row[1])
    profit_increase_month = prev_row[0]



    for r in csvreader:
        
        #number of months calculation
        months.append(r[0])
        
        #net profit and losses for all data
        net_total += int(r[1])
        
        #Profit loss change between months
        pl.append(int(r[1])-int(prev_row[1]))


        if int(r[1]) > profit_increase:
            profit_increase = int(r[1])
            profit_increase_month = r[0]
        
        if int(r[1]) < profit_decrease:
            profit_decrease = int(r[1])
            profit_decrease_month = r[0]

        prev_row = r
    
            

    average = sum(pl)/len(pl)
        

print("Financial Analysis")
print("")
print("-------------------------")
print(f'Total Months: {len(set(months))}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average:.2f}')
print(f'Greatest Increase in Profits: {profit_increase_month} (${profit_increase})')
print(f'Greatest Decrease in Profits: {profit_decrease_month} (${profit_decrease})')

output_path = os.path.join("PyBankOutput.text")
with open(output_path, 'w', newline='') as csvwriter:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    

    csvwriter.write(f"Financial Analysis\n")
    csvwriter.write(f'""\n')
    csvwriter.write(f"-------------------------\n")
    csvwriter.write(f'Total Months: {len(set(months))}\n')
    csvwriter.write(f'Total: ${net_total}\n')
    csvwriter.write(f'Average Change: ${average:.2f}\n')
    csvwriter.write(f'Greatest Increase in Profits: {profit_increase_month} (${profit_increase})\n')
    csvwriter.write(f'Greatest Decrease in Profits: {profit_decrease_month} (${profit_decrease})\n')
