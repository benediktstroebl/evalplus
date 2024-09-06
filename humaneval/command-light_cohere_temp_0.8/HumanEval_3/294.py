```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1,2,3]
    >>> below_zero(operations) 
    True
    >>> operations = [1,2, -4,5]
    >>> below_zero(operations)
    True
    >>> operations = [0,-1,3,4,5]
    >>> below_zero(operations)
    False
    >>> operations = [1,2,3,0,4,5]
    >>> below_zero(operations)
    False
    ``` 
This Python code defines a function `below_zero` that takes a list of operations as input and returns a boolean value indicating whether the balance of the bank account falls below zero at any point. The code then passes various test cases and demonstrates the functionality of the function.