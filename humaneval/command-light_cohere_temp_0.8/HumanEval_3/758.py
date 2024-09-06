```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations) 
    True
    >>> operations = [-3, -2, 1]
    >>> below_zero(operations) 
    False
    """
    balance = 0
    for op in operations:
        if type(op) == int and op <= 0:
            balance -= op
        else:
            return True
    return balance < 0
```