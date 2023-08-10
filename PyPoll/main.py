# import modules 
# Module to create file paths across operating systems 
import os
# Module for reading csv files
import csv
from statistics import mean
totalNumberVotes = 0
candidateNames = []
candidateTotalVotes = []
candidateNameTotal = []
percentageVotes = []
# clean old data showing in the console every time I run the code
# def clean_screen_cmd():
os.system('cmd /c "cls"')


# store the file path associated with the csv file 

datasetFilePath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# file path associated with analysis file
analysisFilepath = os.path.join('PyPoll', 'analysis', 'analysis.txt')
# To Read the file using csv module
with open(datasetFilePath, 'r') as csv_file:
    filereader = csv.reader(csv_file, delimiter=',')
    # print(filereader)
    countCandidates = 0
    countVotes = 0
    # Read the header row first
    fileHeader =next(filereader)
    # print(f"csv Header: {fileHeader}")
    # read each row
    for row in filereader:
        countVotes = countVotes + 1
        candidateNames.append(row[2])
            # candidateTotalVotes.append(row.count(row[2]))
        # print("este es el candidate 1000" + candidateNames[countVotes])
        # print(row)
        countCandidates = countCandidates + 1
    for row2 in range(len(candidateNames)):
        if row2 < 0:
            candidateNameTotal.append(candidateNames[row2])
        else:
            nameCount = 0
            for row3 in range(len(candidateNameTotal)):
                if candidateNames[row2] == candidateNameTotal[row3]:
                    nameCount = 1
                    
                # print(candidateNameTotal[row3])
            if nameCount == 0:
                candidateNameTotal.append(candidateNames[row2])
    countrow4 = 0
    for row4 in candidateNameTotal:
        candidateTotalVotes.append(candidateNames.count(row4))
        percentageVotes.append(round((candidateTotalVotes[countrow4]*100)/countVotes,3))
        countrow4 = countrow4 + 1
        
    zipInfo = list(
        zip(candidateNameTotal, percentageVotes, candidateTotalVotes))
    # 
    # for cN,pV,cTV in zipInfo:
    #     winnerCandidate = max(candidateTotalVotes)
    #     if cTV == winnerCandidate:
    #         nameWinner = cN
            
    #     print(cN,pV,cTV)
    # print("Winner :" + nameWinner)

    # print answers 
    print("\nElection Results")
    print("---------------------------------")
    print("\nTotal Votes: " + str(countVotes))
    print("\n---------------------------------")
    for cN, pV, cTV in zipInfo:
        winnerCandidate = max(candidateTotalVotes)
        if cTV == winnerCandidate:
            nameWinner = cN

        print("\n"+ cN + ": " + str(pV) + "% (" + str(cTV) + ")")
    print("\n---------------------------------")
    print("\nWinner : " + nameWinner)
    print("\n---------------------------------")
    print("\nYour analysis file has been created in the following path :\n", analysisFilepath )
    
    # create analysis file
    analysisFile = open(analysisFilepath, "w")
    analysisFile.write("Election Results")
    analysisFile.write("\n---------------------------------")
    analysisFile.write("\nTotal Votes: " + str(countVotes))
    analysisFile.write("\n---------------------------------")
    for cN, pV, cTV in zipInfo:
        winnerCandidate = max(candidateTotalVotes)
        if cTV == winnerCandidate:
            nameWinner = cN

        analysisFile.write("\n" + cN + ": " + str(pV) + "% (" + str(cTV) + ")")
    analysisFile.write("\n---------------------------------")
    analysisFile.write("\nWinner : " + nameWinner)
    analysisFile.write("\n---------------------------------")
    # analysisFile.write("\nYour analysis file has been created in the following path :\n", analysisFilepath)
    analysisFile.close()
    
    # with open(analysisFilepath, 'w') as textFile:
    #     writer = csv.writer(textFile)
    #     writer.writerow("Financial Analysis")
    #     writer.writerow("---------------------------------")
        # writer.writerow("Total Months: " + str(totalNumberMonths))
        # writer.writerow("Total : $" + str(totalProfitLosses))
        # writer.writerow("Average Change: $ " +
        #                 str(round(profitLossesAverageChange, 2)))
        # writer.writerow("Greatest Increase in Profits: " + str(allInfoIncrease) +
        #                 " ($" + str(round(max(profitLossesChangeV))) + ")")
        # writer.writerow("Greatest Decrease in Profits: " + str(allInfoDecrease) +
        #                 " ($" + str(round(min(profitLossesChangeV))) + ")")
