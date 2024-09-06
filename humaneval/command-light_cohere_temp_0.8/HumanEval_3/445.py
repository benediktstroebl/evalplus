```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, 
    and at that point, the function should return True. Otherwise, it should return False."""
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
``` 
This function below_zero takes a list of operations and checks if the balance ever falls below zero. If it does, it returns True, else False.