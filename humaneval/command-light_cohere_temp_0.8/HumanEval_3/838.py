```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and at that point, the function should return True. Otherwise, it should return False."""
    balance = 0
    for operation in operations:
        if operation < 0:
            return True
        balance += operation
    return False
``` 
This solution checks each operation in the list and returns True if any operation would result in a balance below zero. It will also update the example.