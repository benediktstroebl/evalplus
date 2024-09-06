Here is the self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([2, -4, 5])
    False
    >>> below_zero([0, -2, -1])
    False
    >>> below_zero([100, -20, 0, -100])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function below_zero takes a list of operations, which may be deposit or withdrawal, as input. It keeps track of the balance, which is initialized to zero. The function loops through each operation in the list and adds it to the balance. The function returns True if the balance falls below zero. Otherwise, it returns False.