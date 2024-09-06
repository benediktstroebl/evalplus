Here is the complete Python script with the self-contained function that solves the problem:
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
    >>> below_zero([0, -1, 1, 1, -1])
    False
    >>> below_zero([1, -2, -3, -1, -1, -5])
    True
    >>> below_zero([4, -3, -1, 5, -1, 6])
    False
    >>> below_zero([-5, -3, -1, 1, -1, 1, -1, 6])
    True
    """

    balance = 0
    current = True
    for op in operations:
        if current == 0 and op < 0:
            current = False
        balance += op
    return current
```