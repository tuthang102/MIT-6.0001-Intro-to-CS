# This code did the same thing as in part a with the addition of semi annual raise of the annual salary

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
semi_annual_raise = float(input('Enter the semi-annual raise: '))
current_savings = 0
portion_down_payment = 0.25*total_cost

months = 0
while current_savings <= portion_down_payment:
    monthly_salary = annual_salary / 12
    current_savings = current_savings + monthly_salary*portion_saved + (current_savings*0.04)/12
    months = months + 1
    if months % 6 == 0:
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
print('Number of months:', months)