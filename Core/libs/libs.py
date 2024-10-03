# Library version : 0.1



from datetime import datetime

def to_time(time_str):
    """ Convert time string like ("10:30") to time object"""
    
    return datetime.strptime(time_str, "%H:%M")


def has_time_conflict(course1, course2):
    """ Check conflict in class times"""

    if course1['day'] == course2['day']:
        start1 = to_time(course1['start'])
        end1 = to_time(course1['end'])
        start2 = to_time(course2['start'])
        end2 = to_time(course2['end'])
        

        return not (end1 <= start2 or end2 <= start1)
    
    return False


def count_unique_days(courses):
    """ This function checks the days of classes and deletes repeated classes """
    days = set(course['day'] for course in courses)
    return len(days)


def calculate_idle_time(courses):
    idle_time = 0

    days = {}
    for course in courses:
        day = course['day']
        if day not in days:
            days[day] = []
        days[day].append(course)
    

    for day_courses in days.values():
        sorted_courses = sorted(day_courses, key=lambda x: to_time(x['start']))

        for i in range(len(sorted_courses) - 1):
            end_time = to_time(sorted_courses[i]['end'])
            start_next = to_time(sorted_courses[i+1]['start'])
            idle_time += (start_next - end_time).total_seconds() / 60  
    return idle_time


def duplicate_in_classname(comb) -> bool :
    ls = []
    for i in comb :
        ls.append(i['name'])
    for i in ls :
        if ls.count(i) == 2 :
            return False
            
    return True