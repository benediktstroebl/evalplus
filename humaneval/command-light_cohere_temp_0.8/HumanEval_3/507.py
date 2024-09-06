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
    >>> below_zero([5, 2, 3, -1])
    False
    >>> below_zero([100, 50, -200, -99])
    True
    """
    balance = 0
    for op in operations:
        if op > 0:  # deposit operation
            balance += op
        elif op < 0:  # withdrawal operation
            if balance < 0:
                return True
            balance -= op
    return balance >= 0
```