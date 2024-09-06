```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with a zero balance. Your task is to detect if at any point the balance of the account falls below zero, and at that point, function should return True. Otherwise, it should return False."""
    operations.balance = sum(operations)
    if balance < 0:
        return True
    else:
        return False
``` 
This function below_zero takes a list of operations and determines whether the balance falls below zero at any point, returning True if it does and False if it doesn't. 

The function uses the typing module to provide type hints and the sum function to add the operations together and check for a negative balance.