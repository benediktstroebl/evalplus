Here's a self-contained Python script with a function below_zero that detects if the account balance ever falls below zero in a list of operations:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for operation in operations:
        if operation < 0:
            return True
        balance += operation
    return False
```