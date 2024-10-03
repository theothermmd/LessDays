# Core version : 0.1
import itertools
from libs.excel_driver import excel_driver
from libs.libs import *

def main () -> dict :

    # Get information from Excel file
    excel_file : object = excel_driver("E:\\Book.xlsx")
    courses : list = excel_file.export_data()


    # Get the number of class names (they are unique) to select the unit
    uniq_count : set = set()

    for i in courses :
        uniq_count.add(i['name'])

    # Making all possible combinations with imported classes
    combinations = list(itertools.combinations(courses, len(uniq_count)))

    valid_combinations : list = []
    for comb in combinations:

        if duplicate_in_classname(comb) :
            has_conflict = False
            for i in range(len(comb)):
                for j in range(i+1, len(comb)):
                    if has_time_conflict(comb[i], comb[j]):
                        has_conflict = True
                        break
                if has_conflict:
                    break
            if not has_conflict :

                days_count = count_unique_days(comb)
                idle_time = calculate_idle_time(comb)
                valid_combinations.append((comb, days_count, idle_time))


    valid_combinations.sort(key=lambda x: (x[1], x[2]))
    
    return  { 'plan' : valid_combinations[0][0] , 'days' : valid_combinations[0][1] , 'idle_time' : valid_combinations[0][2]  }

print(main())