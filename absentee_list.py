'''
Call the script using "python3 absentee_list.py --LAB 1 --SECTION 6"

usage: absentee_list.py [-h] [-L LAB] [-S SECTION]

Absentee detector - Attendence

options:
  -h, --help            show this help message and exit
  -L LAB, --LAB LAB     LAB NUM
  -S SECTION, --SECTION SECTION
                        SECTION NUM
'''

import argparse
import pandas as pd

# Argument parsing logic
parser = argparse.ArgumentParser(description='Absentee detector')
parser.add_argument("-L", "--LAB", help="LAB NUM", nargs=1)
parser.add_argument("-S", "--SECTION", help="SECTION: 6/8", nargs=1)
args = parser.parse_args()
LAB_NUM, SECTION = (args.LAB)[0], (args.SECTION)[0]

# Folder structure/Expected File names
ROSTER_FILE = "Rosters/Winter_2023-PHYSICS_0005C____G00"+SECTION+"__-csv.csv"
FOLDER_PATH = "Lab"+LAB_NUM
ATTENDENCE = FOLDER_PATH + '/' + 'G'+SECTION+"_attendance.txt"

# get roster in list format
mydata = pd.read_csv(ROSTER_FILE, header=6)
UID_clean = mydata["UID"].str.replace('-','').replace('\n','')
mydata["UID_clean"] = UID_clean
roster = list(UID_clean)

# compare roster with who attended
with open(ATTENDENCE) as file_:
    for line in file_:
        line_clean = line.replace('-','').replace('\n','')
        # attendance.append(line_clean)
        if line_clean not in roster:
            print(line_clean + " UID not found in roster")
        else:
            roster.remove(line_clean)


# DISPLAY WHO WAS ABSENT
if (roster):
    for student in roster:
        student_details = mydata[mydata['UID_clean'] == student]
        print(student_details['Name'].values[0])
else:
    print("Everyone was present")



