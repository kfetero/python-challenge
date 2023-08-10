# This code will parse the data in budget_data.csv
# and will print the analysis to the terminal and 
# create a text file with the results.
# import modules 
# Module to create file paths across operating systems 
import os
# Module for reading csv files
import csv
from statistics import mean
totalNumberMonths = 0
totalProfitLosses = 0
profitLossesAverageChange = 0.0
dateList = []
profitLossesList = []
# clean old data showing in the console every time I run the code
# def clean_screen_cmd():
os.system('cmd /c "cls"')

# store the file path associated with the csv file 

datasetFilePath = os.path.join('PyBank', 'Resources','budget_data.csv')
# print(datasetFilePath)
# file path associated with analysis file
analysisFilepath = os.path.join('PyBank','analysis', 'analysis.txt')
# To Read the file using csv module
with open(datasetFilePath, 'r') as csv_file:
    filereader = csv.reader(csv_file, delimiter=',')
    # print(filereader)
    countChange = 0
    totalChange = 0
    countItemList = 0
    # Read the header row first
    fileHeader =next(filereader)
    # print(f"csv Header: {fileHeader}")
    # read each row
    for row in filereader:
        countItemList = countItemList + 1
        totalNumberMonths = totalNumberMonths + 1
        totalProfitLosses = totalProfitLosses + int(row[1])
        #add data to the new lists
        dateList.append(row[0])
        profitLossesList.append(int(row[1]))
        #print(row)
    countItemList = 0
    totalChange = 0.0
    profitLossesChangeV = []
    profitLossesChangeD = []
    # add the values of changes to new lists
    for countItemList in range(len(profitLossesList)):
        
        if countItemList > 0:
            profitLossesChangeV.append(float(profitLossesList[countItemList]) - \
                float(profitLossesList[countItemList - 1]))
            profitLossesChangeD.append(dateList[countItemList])
            
    # average change calculation
    profitLossesAverageChange = mean(profitLossesChangeV)
    # Find in the list Greatest Increase and Decrease in Profits
    zipInfo = list(zip(profitLossesChangeD, profitLossesChangeV))
    allInfoIncrease = ''
    for infoIncrease in zipInfo:
        # greatest increase
        if infoIncrease[1] == round(max(profitLossesChangeV)):
            allInfoIncrease = infoIncrease[0]
        # greatest decrease
        if infoIncrease[1] == round(min(profitLossesChangeV)):
            allInfoDecrease = infoIncrease[0]

    # print answers 
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(totalNumberMonths))
    print("Total : $" + str(totalProfitLosses))
    print("Average Change: $ " + str(round(profitLossesAverageChange,2)))
    print("Greatest Increase in Profits: " + str(allInfoIncrease) + " ($" + str(round(max(profitLossesChangeV))) + ")")
    print("Greatest Decrease in Profits: " + str(allInfoDecrease) + " ($" + str(round(min(profitLossesChangeV))) + ")")
    # create file analysis
    analysisFile = open(analysisFilepath, "w")
    analysisFile.write("Financial Analysis")
    analysisFile.write("\n---------------------------------")
    analysisFile.write("\nTotal Months: " + str(totalNumberMonths))
    analysisFile.write("\nTotal : $" + str(totalProfitLosses))
    analysisFile.write("\nAverage Change: $ " + str(round(profitLossesAverageChange, 2)))
    analysisFile.write("\nGreatest Increase in Profits: " + str(allInfoIncrease) + " ($" + str(round(max(profitLossesChangeV))) + ")")
    analysisFile.write("\nGreatest Decrease in Profits: " + str(allInfoDecrease) + " ($" + str(round(min(profitLossesChangeV))) + ")")
    analysisFile.close()
    print("Analysis file has been created in the following path :\n", analysisFilepath)
    
