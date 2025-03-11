# Script to get number of all subchapter tafsirs in order to find missing
# subchapters
import os

file_list = []
for filename in os.listdir():
    if filename.startswith("sc."):
        file_list.append(int(filename.split("_")[0].split(".")[1].strip()))
tafsir_id_list = [29, 54, 71, 68, 4, 51, 96, 52, 83, 67, 10, 90, 105,45,6,84,39,92,89,101,36,31,50,60,102,14,97,66,22,13,65,2,16,75,98,11,103,44,99,42,88,41,40,32,9,7,100,38,15,79,26,12,48,85,95,78,57,24,19,25,94,30,49,47,3,17,20,37,28,33,1,76,5,104,18,55,23,56,91,8]

missing_entries = []

for entry in tafsir_id_list:
    if entry not in file_list:
        missing_entries.append(entry)

print("The following entries are currently missing:\n")
for entry in missing_entries:
    print(entry)
