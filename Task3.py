
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

grace_marks = marks + 5
print("Marks after grace marks:\n", grace_marks)

weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)


employees = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 1],
    "name": [
        "Arun", "Priya", "Rahul", "Divya", "Karthik",
        "Meena", "Suresh", "Anitha", "Arun"
    ],
    "department": [
        "Sales", "HR", "IT", "IT", "IT",
        "HR", "Finance", "Sales", "Sales"
    ],
    "salary": [
        30000, 45000, 60000, np.nan, 90000,
        np.nan, 55000, 40000, 30000
    ],
    "city": [
        "Chennai", "Chennai", "Bangalore", "Chennai",
        "Mumbai", "Chennai", "Bangalore", "Chennai", "Chennai"
    ]
}

pd.DataFrame(employees).to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

print("\nOriginal employee data:")
print(df)


df["id"] = df["id"].astype(int)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")


median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)


df = df.drop_duplicates()


df["salary"] = df["salary"].astype(int)

print("\nCleaned employee data:")
print(df)


df.to_csv("employees_cleaned.csv", index=False)


print("\nData information:")
df.info()

print("\nSalary description:")
print(df.describe())

print("\nUsing loc - Chennai employees:")
print(df.loc[df["city"] == "Chennai", ["name", "city"]])

print("\nUsing iloc - First 3 employees:")
print(df.iloc[0:3, 0:3])

print("\nEmployees with salary above 50000:")
print(df[df["salary"] > 50000])


summary = df.groupby("department").agg(
    headcount=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment summary:")
print(summary)

print("\nHeadcount:")
for department, count in summary["headcount"].items():
    print(f"{department}: {count}")



departments = pd.DataFrame({
    "department": ["Sales", "HR", "IT", "Finance", "Marketing"],
    "head": [
        "Ravi", "Priya", "Kumar", "Meena", "Anand"
    ],
    "budget": [500000, 300000, 800000, 400000, 200000]
})

departments.to_csv("departments.csv", index=False)

dept_df = pd.read_csv("departments.csv")

inner = pd.merge(df, dept_df, on="department", how="inner")
print("\nINNER JOIN:")
print(inner)


left = pd.merge(df, dept_df, on="department", how="left")
print("\nLEFT JOIN:")
print(left)


outer = pd.merge(df, dept_df, on="department", how="outer")
print("\nOUTER JOIN:")
print(outer)


no_employees = dept_df[
    ~dept_df["department"].isin(df["department"])
]

print("\nDepartments with no employees:")
print(no_employees)


os.makedirs("charts", exist_ok=True)


plt.figure()
summary["average_salary"].plot(
    kind="bar", label="Average Salary"
)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.close()

print("Insight: Compare average salaries across departments.")


plt.figure()
plt.hist(df["salary"], bins=5, label="Employees")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("charts/histogram.png")
plt.close()

print("Insight: The histogram shows how employee salaries are distributed.")


plt.figure()
plt.scatter(df["id"], df["salary"], label="Employees")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/scatter_plot.png")
plt.close()

print("Insight: The scatter plot compares individual employee salaries.")


plt.figure()
plt.plot(df["id"], df["salary"], marker="o", label="Salary")
plt.title("Employee Salary Comparison")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.close()

print("Insight: The line chart shows salary changes across employee IDs.")