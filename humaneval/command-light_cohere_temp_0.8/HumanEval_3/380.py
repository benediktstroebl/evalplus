Here's the provided Python script with the self-contained function `below_zero` that solves the problem you've described: 

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
    >>> below_zero([6, 7, 8, 9])
    False
    """
    for op in operations:
        if op < 0:
            return True
    return False
``` 

This function takes a list of deposit and withdrawal operations as an argument and uses a loop to iterate through each operation. If it encounters an operation that is negative, it returns True, indicating that the balance has fallen below zero. If all operations are positive and non-negative, it returns False, indicating that the balance never fell below zero.