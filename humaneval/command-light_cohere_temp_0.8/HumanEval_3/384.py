Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([5, -1, 3, -2, 1])
    False
    >>> below_zero([0, 1, -3, 2])
    True
    """

    # Detects if the balance ever falls below zero
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
This script provides a self-contained function that solves the problem of checking if a series of deposits and withdrawals result in a negative balance at any point. It also passes the result tests to ensure correctness.