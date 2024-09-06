Here's the self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0, 1, 2, -4, 5]
    >>> below_zero(operations)
    False
    >>> operations = [5, 0, -3, 2, 1]
    >>> below_zero(operations)
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This script defines a function called `below_zero` that takes a list of operations as input. It iterates through operations, adds each operation to the balance, and then checks if the balance is less than zero. The function returns `True` if the balance is less than zero, and `False` otherwise.