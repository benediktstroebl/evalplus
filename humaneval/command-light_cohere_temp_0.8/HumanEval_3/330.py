Here's a self-contained Python script that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [[-4, 5, 1, 2]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3, -4])
    False
    >>> below_zero([0, 1, -4, 5])
    False
    >>> below_zero([9, 2, -4, -5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
The function below_zero takes a list of operations as input. It initializes a problem with an initial balance of 0. The function then iterates over each operation in the list and adds the operation to the balance.

The function returns True if the balance falls below 0 at any point during the iteration, and False otherwise.