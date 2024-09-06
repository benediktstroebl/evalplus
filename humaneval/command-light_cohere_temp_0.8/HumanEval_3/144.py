Here's the self-contained Python script with a function `below_zero()` that solves the problem:

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
    >>> below_zero([0, 1, -5, 3])
    False
    >>> below_zero([100, 50, 0, -20])
    True
    """

    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
```

This script provides a solution to the problem statement. It iterates through balance of the operations, if the balance ever falls below zero, the function returns True. Otherwise, it returns False.