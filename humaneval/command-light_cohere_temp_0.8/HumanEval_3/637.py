```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 1, -2, 3])
    False
    >>> below_zero([1,2, -1,3])
    True
    >>> below_zero([9,8,7,6])
    False
    """
    operations.count = 0
    operations = sorted(operations)
    balance = 0
    for num in operations:
        if num < 0:
            balance -= num
        else:
            count += num
    if balance < 0:
        return True
    else:
        return False
```