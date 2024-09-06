```Python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and at that point function should return True. Otherwise, it should return False.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([10, -4, 5])
    False
    >>> below_zero([1, 2, 3, -4])
    True
    """
    operations.sort()
    imbalance: 0
    for i, num in enumerate(operations):
        if num < 0 and imbalance != 0:
            return True
        imbalance += num
    return False
```