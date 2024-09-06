```Python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, -2, 3, -5])
    False
    >>> below_zero([10, -10, -30, 20])
    True
    >>> below_zero([2, -5, 3, -8])
    False
    """
    for op in operations:
        if op < 0:
            return True
    return False
```  This Python function 'below_zero' solves the given problem. It takes a rate-through a list of operations and checks if any operation is negative, which would cause the balance to fall below zero. If the loop completes without any negative operation, the function returns False, indicating no balance below zero. Otherwise, it returns True, indicating that the balance is below zero at some point in the list of operations.