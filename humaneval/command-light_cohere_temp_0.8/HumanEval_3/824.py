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
    >>> below_zero([4, -2, 3, -1])
    False
    >>> below_zero([2, -8, 1, -1])
    True
    >>> below_zero([100, 100, -3, -3])
    False
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```