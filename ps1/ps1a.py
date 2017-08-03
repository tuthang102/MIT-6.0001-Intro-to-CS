# This code calculates the # of months needed to save money for the down payment of your dream house

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
current_savings = 0
portion_down_payment = 0.25*total_cost  # down payment is 25% of the total cost
monthly_salary = annual_salary/12       # monthly salary = annual salary/12
months = 0
while current_savings <= portion_down_payment:
        months = months + 1
        current_savings = current_savings + monthly_salary*portion_saved + (current_savings*0.04)/12
print('Number of months:', months)