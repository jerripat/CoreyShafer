

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@gmail.com'
        self.pay = pay
        
        Employee.num_of_employees += 1
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
        
emp_1 = Employee('John', 'Doe', 10000)
emp_2 = Employee('Jane', 'Doe', 20000)

print(Employee.raise_amount)
print(emp_2.raise_amount)
        
        