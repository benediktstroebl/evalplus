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
    >>> below_zero([3, 2, -4, 5])
    False
    >>> below_zero([0, 1, 2, 3])
    True
    >>> below_zero([100, 100, 1, -100])
    False
    """
    operations.count_negative = 0
    operations_count_positive = 0
    for operation in operations:
        if operation < 0:
            operations.count_negative += 1
    count_positive += 1
    return (operations.count_negative > 0 and operations.count_positive == 0)
```