Script to make the attendence simpler for Physics 5C.
1. This will tell you if someone who is in your roster didn't show up.
2. If extra people showed up.

Dependencies: pandas

You need:
1. The UIDs in a file called "G<SECTION_NUM>_attendance.txt" placed under "Lab<LAB_NUM>" folder
2. Your class Roster (See Notes)

CMD to run(for LAB_NUM=1, SECTION_NUM=6):
1. Navigate to the folder where you have cloned this
2. python3 absentee_list.py --LAB 1 --SECTION 6

Notes:
1. your class roster is available in MyUCLA. MyUCLA>Faculty>Class Roster>Roster Download>Comma Seperated
    Place the downlaoded file in "Rosters" folder
    Place the attendence(UIDs only) under Lab<LAB_NUM>/G<SECTION_NUM>_attendance.txt
    
2. if the UIDs have a - in them, then that is fine. the script will correct for that.
