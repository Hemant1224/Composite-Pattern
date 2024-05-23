# Scenario
# Employee: Represents a simple employee.
# Manager: Represents a manager who can have subordinate employees.
# Both employees and managers can provide their details, but a manager can also list details of their 


from abc import ABC, abstractmethod

# Component
class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def show_details(self):
        print(f"Name: {self.name}, Position: {self.position}")

class Designer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def show_details(self):
        print(f"Name: {self.name}, Position: {self.position}")

# Composite
class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add(self, employee):
        self.subordinates.append(employee)

    def remove(self, employee):
        self.subordinates.remove(employee)

    def show_details(self):
        print(f"Name: {self.name}, Position: {self.position}")
        for subordinate in self.subordinates:
            subordinate.show_details()

# Client code
dev1 = Developer("Alice", "Senior Developer")
dev2 = Developer("Bob", "Junior Developer")
designer = Designer("Charlie", "Designer")

manager = Manager("David", "Development Manager")
manager.add(dev1)
manager.add(dev2)
manager.add(designer)

# Printing details
manager.show_details()
