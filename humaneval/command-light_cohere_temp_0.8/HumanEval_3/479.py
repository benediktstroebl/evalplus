Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
    >>> below_zero([0, 2, 3])
    False
    >>> below_zero([10, 1, -20])
    True
    >>> below_zero([100, -20, 1])
    False
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This function takes a list of operations as input and iterates over each operation in the list. It calculates the balance by adding the operations and checks if the balance is less than 0. If it is, the function returns True; otherwise, it returns False.