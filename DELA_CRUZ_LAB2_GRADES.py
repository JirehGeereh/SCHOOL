# PAGBABAGO SA MGA CODE PAULIT ULIT UNA KAILANGAN ICLONE



# Initialization for the final grade, equivalent, and student name.
final_grade = 0
equivalent_grade = 0
student_name = ""

# Getting inputs for student name, final quizzes, final research/assignment, final project and, final exam.
student_name = str(input("Enter Student Name: "))
final_quizzes = float(input("Enter Final Quizzes Grade: "))
final_research = float(input("Enter Final Research/Assignment Grade: "))
final_project = float(input("Enter Final Project Grade: "))
final_exam = float(input("Enter Final Exam Ratings: "))

# Setting grades to not exceed 100.
if final_quizzes or final_research or final_project or final_exam > 100:
    print("Invalid Grades.")

# Setting formula for the computation of final grade, and formula for rounding off the final grade.
final_grade = (0.30 * final_quizzes) + (0.10 * final_research) + (0.40 * final_exam) + (0.20 * final_project)
final_grade_rounded = round(final_grade, 0)


# Setting conditions to the equivalent grade of final grade using function.
def get_equivalent_grade():
    if final_grade_rounded > 100:
        return "Invalid Grade. No Grade should exceed 100. Please Try Again"
    elif final_grade_rounded >= 98:
        return 4.00
    elif final_grade_rounded >= 95:
        return 3.75
    elif final_grade_rounded >= 92:
        return 3.50
    elif final_grade_rounded >= 89:
        return 3.25
    elif final_grade_rounded >= 86:
        return 3.00
    elif final_grade_rounded >= 83:
        return 2.75
    elif final_grade_rounded >= 80:
        return 2.50
    elif final_grade_rounded >= 77:
        return 2.25
    elif final_grade_rounded >= 74:
        return 2.00
    elif final_grade_rounded >= 71:
        return 1.75
    elif final_grade_rounded >= 68:
        return 1.50
    elif final_grade_rounded >= 64:
        return 1.25
    elif final_grade_rounded >= 60:
        return 1.00
    else:
        return 0.00


# Preparing condition function to be a variable for equivalent grade.
# Conditions cannot be put without function as it will not follow the flowchart, it would rather be displayed at the
# display section.
equivalent_grade = get_equivalent_grade()

# Displaying student name, final quizzes, final research/assignment, final project and, final exam, final grade, and
# equivalent grade.
print("Student Name:", student_name)
print("Final Quizzes Grade:", final_quizzes)
print("Final Research/Assignment Grade:", final_research)
print("Final Project Grade:", final_project)
print("Final Exam Ratings:", final_exam)
print("Final Grade:", final_grade_rounded)
print("Equivalent Grade:", equivalent_grade)
