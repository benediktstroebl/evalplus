Here is a self-contained Python script with a function that solves the problem and passes the tests provided:
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
    >>> below_zero([5, -4, 1, 2])
    False
    >>> below_zero([1, -3, -2, -1])
    True
    >>> below_zero([1, -1, 0, 0])
    False
    >>> below_zero([100, -100, 0, 0])
    False
    """
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
```