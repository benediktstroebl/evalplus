```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks if the operations in the list will cause the balance to go below zero.

    : Also returns True if balance ever becomes negative, otherwise False.
    """
    list comprehension is used to convert the operations list to a deposit/withdraw series of numbers.
    operations = list(sorted(operations, reverse=True))
    for i in range(len(operations) - 1):
        if operations[i] > 0 and operations[i+1] < 0:
            return True
    return False
```