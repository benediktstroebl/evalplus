Here's a self-contained Python script that defines a function `below_zero` that checks whether the balance of a bank account falls below zero, and tests it using the provided input:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    return operations[0] < 0  # Deposits and withdrawals are non-negative
```

This function takes a list of operations as input and uses list comprehension and the < operator to check if the first element is less than zero, which corresponds to the first deposit or withdrawal. The function returns True if the balance falls below zero, and False otherwise.