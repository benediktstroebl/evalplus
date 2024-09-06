```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([0, 2, -4, 5])
    False
    >>> below_zero([1, 2, 3, -4, 5])
    True
    >>> below_zero([1, 2, -3, 4, 5])
    False
    >>> below_zero([1, 2, -4, -5, 6])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The above-given code defines a Python function `below_zero` which takes a list of operations as an argument. The function calculates the expected behaviour of the account balance after all operations, and returns `True` if it's less than zero, and `False` otherwise.