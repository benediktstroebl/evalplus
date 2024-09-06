Here's the code with a self-contained function that solves the problem of detecting if the balance of a bank account ever falls below zero:
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
    >>> below_zero([0, 2, 3, -1])
    False
    >>> below_zero([100, -200, 300, -100])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function below_zero takes a list of operations as input and iteratively adds each operation to a running total of deposits and withdrawals. The function then returns True if the balance falls below zero, otherwise it returns False.