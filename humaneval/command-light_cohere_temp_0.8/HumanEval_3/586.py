```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3, -4])
    False
    >>> below_zero([0, 1, -4, 5])
    False
    >>> below_zero([100, 100, -4, 5])
    True
    >>> below_zero([1, 2, -3, -1])
    False
    """
    # Initialize a flag
    balance = 0
    flag = False
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        # If the balance goes below zero, return True
        if balance < 0:
            flag = True
            break
    # If we didn't find a balance below zero, return False
    return flag
```