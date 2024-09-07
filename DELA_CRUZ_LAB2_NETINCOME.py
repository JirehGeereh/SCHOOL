# Initialization for the Employee Name, Department, Net Income, Gross Income, Total Deduction, and Pag-ibig Contribution
emp_name = ""
department = ""
net_income = 0
gross_income = 0
total_deduction = 0
pagibig_contri = 100.00

# Getting inputs for employee name, rate per hour, number of hours per day, number of days per week, and number of weeks
# per month.
emp_name = str(input("Enter Employee's Name: "))
department = str(input("Enter Employee's Department: "))
rate_per_hour = float(input("Enter Employee's Rate Per Hour: "))
num_hrs_per_day = float(input("Enter Employee's Working Hours Per Day: "))
num_days_per_week = int(input("Enter Employee's Working Days Per Week: "))
num_weeks_per_month = int(input("Enter Employee's Working Weeks Per Month: "))

# Setting formula for the computation of gross income
gross_income = rate_per_hour * num_hrs_per_day * num_days_per_week * num_weeks_per_month


# Setting condition for the value of SSS Contribution based on gross income.
def get_sss_contri():
    if gross_income <= 20000:
        return 125.75
    elif gross_income <= 50000:
        return 2200.50
    elif gross_income <= 75000:
        return 4800.00
    else:
        return 5800.00


# Setting condition for the value of Philhealth Contribution based on gross income.
def get_philhealth_contri():
    if gross_income <= 20000:
        return 100.00
    elif gross_income <= 50000:
        return 1200.00
    elif gross_income <= 75000:
        return 6800.00
    else:
        return 8800.00


# Preparing condition functions to be a variable for SSS Contribution and Philhealth Contribution.
# Conditions cannot be put without function as it will not follow the flowchart, it would rather be displayed at the
# display section.
sss_contri = get_sss_contri()
philhealth_contri = get_philhealth_contri()

# Setting formula for the computation of total deduction and net income
total_deduction = sss_contri + philhealth_contri + pagibig_contri
net_income = gross_income - total_deduction

# Displaying the Name of the Employee, Department, Net and Gross Income, Total Deduction.
print("Employee Name:", emp_name)
print("Department of Employee:", department)
print("Net Income:", net_income)
print("Gross Income:", gross_income)
print("Total Deduction:", total_deduction)
