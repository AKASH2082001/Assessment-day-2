name = []
age = []
designation = []
salary = []
n = int(input("number of employee:"))
for i in range(n):
    name_1 = input("employee name:")
    age_1 = input("employee age:")
    designation_1 = input("employee designation:")
    salary_1 = input("employee salary:")
    name.append(name_1)
    age.append(age_1)
    designation.append(designation_1)
    salary.append(salary_1)
    print(name)
    print(age)
    print(designation)
    print(salary)