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
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
```
The function below_zero takes a list of operations and iteratively performs each operation, adjusting the balance. If the balance ever falls below 0, the function returns True, otherwise, it returns False.