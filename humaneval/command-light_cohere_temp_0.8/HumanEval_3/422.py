Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    # Sort operations in descending order
    operations.sort(reverse=True, operations)
    # Initialize balance with 0
    balance = 0
    for op in operations:
        # If the balance is now negative, return True
        if balance < 0:
            return True
        # Add operation to balance
        balance += op
    return False
```
This script defines a function `below_zero` that takes a list of operations (deposit and withdrawal) as input. It then sorts the general operations in descending order and for each operation, it checks if the balance goes below zero, if so, it returns True, otherwise, it adds the operation to the balance and returns False.