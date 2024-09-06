```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, -4, 5]
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1,2,3,4,5])
    False
    >>> below_zero([0,1,2,3])
    True
    >>> below_zero([100,2,3])
    False
    >>> below_zero([100,1,3,4])
    False
    """
    current = 0
    for op in operations:
        current += op
    if current < 0:
        return True
    return False
```  The script defines a function called `below_zero` that takes a list of operations as an argument and returns a boolean value indicating whether the account balance fell below zero at any point during the operations.