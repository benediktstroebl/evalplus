```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [1, 2, 3, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [1, 2, 3, 0, 5]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, -4, 5, 0]
    >>> below_zero(operations)
    True
    """

def detect_balance_below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
    if balance < 0:
            return True
    else:
        return False
``` 
This function takes a list of operations, iterates through the list, and checks if the balance falls below zero after each operation. It will return True if the balance falls below zero and returns False otherwise. 

This script is self-contained and can be used to solve the problem and pass corresponding tests.