```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [-1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0, 1, -10, 2]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, 3, -5]
    >>> below_zero(operations)
    True
    ```