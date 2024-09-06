Here's the solution code:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([5, -1, -4, 3])
    False
    >>> below_zero([0, -2, -100, 0])
    True
    """
    for op in operations:
        if op < 0:
            return True
    return False
```
The function below_zero takes a list of operations as input and returns a boolean value that indicates whether the balance of the account falls below zero at any point. The function iterates through the the operations and checks if any operation is negative. If so, it returns True. Otherwise, it returns False.