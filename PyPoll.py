# the data we need to retrieve
#1. the total number of votes cast
#2. a complete list of candidates who received votes
#3. the percentage of votes each candidate won
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote
import csv
import os 
print(os.getcwd())
file_to_load = os.path.join("Resources", "election_results.csv")
print(os.getcwd())
print(file_to_load)
with open(file_to_load) as f : 
    #as f = the file that's saved --> eg. f.readline 
    print("election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Counties in the Election\n------\nArapahoe\nDenver\nJefferson")
outfile.close()

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

   
