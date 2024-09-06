```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, 3]
    >>> below_zero(operations)
    True
    >>> operations=[1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations=[0, 1, -1, -2]
    >>> below_zero(operations)
    False
    >>> operations=[9, 2, -1, -2]
    >>> below_zero(operations)
    True
    ``` 
This script defines a function `below_zero` that takes a list of operations and returns a boolean indicating if the balance of the account ever fell below zero. It uses a this approach, it's simple and straightforward, but it solves the problem effectively.