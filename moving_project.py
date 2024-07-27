# pay in hours for employees
pay_scale = {
    'Alex' : 25.50,
    'Bill' : 25,
    'Charlie' : 22,
    'Edward' : 20,
    'Fred' : 18

}

#mileage compensation for miles driven on personal vehicle
mileage_rate = .30

#asks who worked today
def worked_today():
    employees = input('Enter the name of who worked today seperated by commas: ').split(",")
    return [employee.strip() for employee in employees]

#asks amount of hours and miles driven
def hours_miles(pay_scale, employees):
    hours_worked = {}
    miles_driven = {}
    for employee in employees:
        if employee in pay_scale:
            while True:
                try:
                    hours = float(input(f"Enter the amount of hours worked for {employee}:"))
                    hours_worked[employee]= hours
                    break
                except ValueError:
                    print('invalid input, please try again')
            while True:
                try:
                    miles = float(input(f"Enter the amount of miles driven for {employee}:"))
                    miles_driven[employee]= miles
                    break
                except ValueError:
                    print('invalid input, please try again')
        else:
            print(f"{employee} not found in pay_scale dictionary")
    return hours_worked , miles_driven

#calculcates total pay
def calculate_total_pay(pay_scale, hours_worked, miles_driven, mileage_rate):
    total_pay = {}
    for employee in hours_worked:
        if employee in miles_driven:
            wage_pay = pay_scale[employee] * hours_worked[employee]
            mileage_pay = miles_driven[employee] * mileage_rate
            total_pay[employee] = wage_pay + mileage_pay
        else: 
            total_pay[employee] = 'Mileage data unavaliable'
    return total_pay

def final(total_pay):
    for employee, pay in total_pay.items():
        if isinstance(pay, str):
            print(f"{employee}: {pay}")
        else:
            print(f"{employee}: ${pay:.2f}")

employee_hours = worked_today()
hours_worked , miles_driven = hours_miles(pay_scale , employee_hours)
total_pay = calculate_total_pay(pay_scale, hours_worked, miles_driven, mileage_rate)
final(total_pay)