# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
outputpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data_result.txt')

'Variables to be calculated'
total_no_months = 0
total_net_profit_loss = 0
avg_profit_loss = 0
greatest_increase_in_profit_amount = 0
greatest_increase_in_profit_month = ""
greatest_decrease_in_profit_amount = 0
greatest_decrease_in_profit_month = ""
total_amount_changes = 0

previous_month_amount = 0
change_in_amount = 0


with open(csvpath, newline='') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    'read the header'
    csv_header = next(csvreader)

    for row in csvreader:
        'total months'
        total_no_months = total_no_months + 1
        total_net_profit_loss = total_net_profit_loss + float( row[1])

        'change between previous month'
        'There is no change in first month'
        if total_no_months == 1:
            change_in_amount = 0
        else:
            change_in_amount = float(row[1]) - previous_month_amount

        'To do the total of change_in_amounts for finding net'

        total_amount_changes = total_amount_changes + change_in_amount

        'greatest increase'
        if change_in_amount > greatest_increase_in_profit_amount:
            greatest_increase_in_profit_amount = change_in_amount
            greatest_increase_in_profit_month = row[0]

        if change_in_amount < greatest_decrease_in_profit_amount:
            greatest_decrease_in_profit_amount = change_in_amount
            greatest_decrease_in_profit_month = row[0]

        'To store previous month profit/loss'
        previous_month_amount = float(row[1])

'There is no change in first month (between months - total months - 1)'
avg_profit_loss = total_amount_changes / (total_no_months -1)

with open(outputpath, "w") as outputfile:
    print(f"Total Months: {total_no_months}")
    print("Total: total_net_profit_loss:${0:.0f}".format(total_net_profit_loss))
    print("Average Change:${0:10.2f}".format(avg_profit_loss))
    print("Greatest Increase in Profits: {0} (${1:.0f})".format(greatest_increase_in_profit_month, greatest_increase_in_profit_amount))
    print("Greatest Decrease in Profits: {0} (${1:.0f})".format(greatest_decrease_in_profit_month, greatest_decrease_in_profit_amount))

    outputfile.write(f"Total Months: {total_no_months} \n")
    outputfile.write("Total: total_net_profit_loss:${0:.0f} \n".format(total_net_profit_loss))
    outputfile.write("Average Change:${0:10.2f} \n".format(avg_profit_loss))
    outputfile.write("Greatest Increase in Profits: {0} (${1:.0f}) \n".format(greatest_increase_in_profit_month, greatest_increase_in_profit_amount))
    outputfile.write("Greatest Decrease in Profits: {0} (${1:.0f}) \n".format(greatest_decrease_in_profit_month, greatest_decrease_in_profit_amount))

    outputfile.close()