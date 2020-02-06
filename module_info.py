# Returns the number of completed assessments for the module given
def get_completed_assess(mod):
    completed = 0
    for assess in mod["assessments"]:
        if assess["complete"]:
            completed += 1
    return completed

# Returns the percentage from the marks gotten for a given assessment
def get_assess_percentage(assess):
    return (assess["mark"] * 100) / assess["max_mark"]

# Converts a percentage into the equivalent uni grade
def perc_to_grade(perc):
    if perc >= 70:
        return "1"
    elif perc >= 60:
        return "2:1"
    elif perc >= 50:
        return "2:2"
    elif perc >= 40:
        return "3"
    else:
        return "Fail"

# Calculates the average grade of all completed assessments in a module
# If no assessments complete, returns None to avoid divide by zero error
def get_average_grade(mod):
    grade = 0
    num_assess = 0
    for assess in mod["assessments"]:
        if assess["complete"]:
            num_assess += 1
            grade += get_assess_percentage(assess)

    if num_assess > 0:
        return round(grade / num_assess, 1)
    else:
        return None

def get_total_grade(mod):
    grade = 0
    num_assess = len(mod["assessments"])
    for assess in mod["assessments"]:
        grade += get_assess_percentage(assess)
    return round(grade / num_assess, 1)
