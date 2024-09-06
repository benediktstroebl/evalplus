Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, -1, 3, 4])
    False
    >>> below_zero([100, 2, -100, -3])
    False
    """

    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        elif balance < 0:
            return True
    return False
```