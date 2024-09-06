```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, 
    and at that point, the function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    operations = sorted(operations) 
    balance = 0 
    for op in operations:
        if balance < 0: 
            return True
        balance += op
    return False
```