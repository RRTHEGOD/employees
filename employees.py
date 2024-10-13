"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Rahul Rathan and Nawal Osama, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1:rr53829
UT EID 2:no4535
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


import random

class Employee:
    def __init__(self, name, manager, salary, savings):
        if type(self) is Employee:
            raise TypeError("Cannot instantiate abstract class Employee.")
        self.name = name
        self.manager = manager
        self.salary = salary
        self.savings = savings
        self.happiness = 50
        self.performance = 75
        self.is_employed = True

    def daily_expense(self):
        self.happiness -= 1
        self.savings -= 60
        if self.savings < 0:
            self.savings = -self.savings

    def work(self):
        pass

    def interact(self, other_employee):
        if not isinstance(other_employee, Employee):
            return
        self.happiness += 1  # Happiness increases with interaction
        self.performance += 2  # Optional: Improve performance with interaction


class Manager(Employee):
    def __init__(self, name, manager, salary, savings):
        super().__init__(name, manager, salary, savings)
        self.relationships = {}
        self.performance = min(100, max(0, self.performance))

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value):
        self._performance = min(max(0, value), 100)

    def work(self):
        self.performance += random.randint(-10, 10)

    def daily_expense(self):
        super().daily_expense()


class TemporaryEmployee(Employee):
    def __init__(self, name, manager, salary, savings):
        super().__init__(name, manager, salary, savings)

    def work(self):
        self.performance += random.randint(-10, 10)


class PermanentEmployee(Employee):
    def __init__(self, name, manager, salary, savings):
        super().__init__(name, manager, salary, savings)

    def work(self):
        self.performance += random.randint(-5, 5)
