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
    >>> below_zero([0, 1, -3])
    False
    >>> below_zero([-5000, -3000, 3000])
    True
    >>> below_zero([-1, -2, 3000, 5000])
    False
    """
    # Using recursive approach to solve the problem
    balance = 0
    is_below_zero = True
    for operation in operations:
        if operation < 0:
            is_below_zero = True
        if is_below_zero:
            break
        balance += operation
    return is_below_zero
```