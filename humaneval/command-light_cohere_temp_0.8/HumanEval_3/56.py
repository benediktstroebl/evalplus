```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
``` 
This approach iterates through a list of operations and maintains a balance. At any point where the set, the balance will be less than zero, the function will return True.