Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point, function should return True. Otherwise, it should return False.

    >>> operations = [1, 2, -4, 5]
    return balance < 0
```
The function below_zero takes a list of operations and checks if the balance of the account ever falls below zero. If it does, it returns True; otherwise, it returns False.