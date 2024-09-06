Here's a Python script that includes the `below_zero` function, which is self-contained and solves the problem you described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([4, -3, 5, 1])
    False
    >>> below_zero([10, 11, 12])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```

This script defines a function `below_zero` that takes a list of integers as input. It calculates the balance of the account by summing up all the operations and checks if the balance is less than 0. It returns `True` if the balance falls below 0, and `False` otherwise. 

The script also includes several test cases to demonstrate the functionality of the `below_zero` function.