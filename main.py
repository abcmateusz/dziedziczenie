class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayInfo(self):
        print(f"Pracownik: {self.name}, Wynagrodzenie: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, teamSize=0):
        super().__init__(name, salary)
        self.teamSize = teamSize

    def displayInfo(self):
        print(f"Pracownik: {self.name}, Wynagrodzenie: {self.salary}, Zespół: {self.teamSize} osób")

class Director(Manager):
    def __init__(self, name, salary, teamSize, department):
        super().__init__(name, salary, teamSize)
        self.department = department

    def displayInfo(self):
        print(f"Pracownik: {self.name}, Wynagrodzenie: {self.salary}, Zespół: {self.teamSize} osób, Dział: {self.department}")

def main():
    employee = Employee("Jan Kowalski", 4000)
    employee.displayInfo()

    manager = Manager("Anna Nowak", 7000, 10)
    manager.displayInfo()

    director = Director("Marek Wiśniewski", 12000, 20, "IT")
    director.displayInfo()

if __name__ == "__main__":
    main()
