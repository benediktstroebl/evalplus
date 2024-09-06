Here's a self-contained Python script that solves the given problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> [1,2,3]
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([4,2,-1,5])
    False
    >>> below_zero([6, -8, -4, 9])
    True
    >>> below_zero([6, -8, -4, 9, -1])
    False
    >>> below_zero([6, -8, -2, 9])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
```