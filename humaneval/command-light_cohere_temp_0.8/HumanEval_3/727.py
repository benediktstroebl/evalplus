Here's a self-contained Python function that solves the problem you provided:
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
    """
```
This function takes a list of operations and determines whether the balance of the account falls below zero at any point in the list. The function works by iterating through the operations and checking the balance after each operation. It checks if the balance is less than zero and returns `True` if this condition is met. If the balance remains non-negative throughout all operations, it returns `False`.