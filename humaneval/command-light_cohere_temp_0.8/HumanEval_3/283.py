```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ Detects whether the balance of the account falls below zero at any point 
    in the operations given. Returns True if it balance falls below zero at any point, 
    otherwise False."""
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
``` 
This script defines a `below_zero` function that takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function uses a balance variable to keep track of the account balance and iterates over the operations, checking if the balance falls below zero at any point.