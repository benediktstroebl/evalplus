Here's a self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and at that point, function should return True. Otherwise, it should return False."""
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
``` 
The function checks through a list of deposit and withdrawal operations, and returns `True` if the balance ever falls below zero, otherwise it returns `False`.