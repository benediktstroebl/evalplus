```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
# Test the function
# Test the function passing different operations list
print(below_zero([1, 2, -4, 5]))  # Output: True
print(below_zero([5, -4, 1, 2]))  # Output: False
print(below_zero([0, -10, -8]))  # Output: True
``` 
This Python script defines a function `below_zero` that checks whether the balance of a bank account falls below zero or not. The function takes a list of operations (deposits and withdrawals) as input and iterates over the list, updating the balance accordingly. 

It returns `True` if the balance falls below zero at any point, and `False` otherwise. 
This function can be used to check if a given list of operations will cause the balance to go below zero.