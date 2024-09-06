Here is a Python script that includes the self-contained function `below_zero` that solves the problem:

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
    >>> below_zero([0, 1, 2, -3])
    False
    >>> below_zero([10, 20, 30, 40])
    True
    """
    for op in operations:
        if op < 0:
            return True
    return False
```

This script defines a function below_zero that takes a list of integers as an argument. The function loops through the required operations to detect if any operation will cause the balance to fall below zero. It returns True if it.  It returns True after the if any operation is less than zero, and False otherwise.