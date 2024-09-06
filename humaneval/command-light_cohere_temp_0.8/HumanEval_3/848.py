```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([0, 2, -4, 5])
    False
    >>> below_zero([1, 2, -4, 5, -1])
    False
    >>> below_zero([-50, -20, -40, -30])
    True
    """
    operations = sorted(operations)
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```