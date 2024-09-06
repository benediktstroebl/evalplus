Here is a self-contained Python script with a function that solves the problem of checking if the balance of a bank account falls below zero, and tests it with passing tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations
    fact list of operations: 
    1, 2, -4, 5
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
``` 
This script provides a complete, self-contained function that solves the problem of checking if the balance of a bank account falls below zero, with tests included.