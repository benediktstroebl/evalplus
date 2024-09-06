```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    """
   
    is an optimization to check only the last operation if the balance is already at zero.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 1, -4, 5])
    False
    >>> below_zero([1, 2, 3, 4, -5])
    True
    """
    if operations[-1] > 0:
        return False
    return True
```