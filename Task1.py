import csv

#Bonus Method
def bonus(salary, rate=0.1,*extras,**options):
    total= (salary*rate)+sum(extras)

    if("cap" in options):
        total=min(total,options["cap"])
    
    return total

print(bonus(50000,1,9000,1200,cap=60000))    

class InvalidSalaryError(Exception):
    pass

class Employee:
 def __init__(self,name,salary,):
    if salary<0:
       print("invalid salary")
    self.name=name
    self.salary=salary
 def annual_salary(self):
   return self.salary*12
 def get_details(self):
    return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )

try:
    employee = Employee("Test Employee", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")          

with open("employee.csv","r",newline="",encoding="utf-8-sig") as file:
    reader=csv.DictReader(file)
    high_salary_names = [
    employee["Name"]
    for employee in reader
    if int(employee["Salary"]) > 50000
    ]

print("Above 50000:", high_salary_names)

with open("employee.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    raised_salaries = list(
        map(
            lambda row: round(int(row["Salary"]) * 1.10, 2),
            reader
        )
    )

print("Salaries after 10% raise:", raised_salaries)

with open("employee.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    chennai_rows = filter(
        lambda row: row["City"] == "Chennai",
        reader
    )

    chennai_names = [row["Name"] for row in chennai_rows]

print("Chennai:", chennai_names)

with open("employee.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = int(row["Salary"])

        if salary == 0:
            continue

        if salary > 85000:
            break

        print("Processed salary:", salary)

employee1 = Employee("Arun", 30000)
manager1 = Manager("Priya", 80000, 5)

print(employee1.get_details())
print("Annual salary:", employee1.annual_salary())
print(manager1.get_details())        