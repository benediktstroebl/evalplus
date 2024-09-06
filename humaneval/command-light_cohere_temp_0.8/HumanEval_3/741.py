```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, 
    and at that point, the function returns True. Otherwise, it returns False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations) 
    True
    """
    operations.any balance = 0
    balance = operations[-1]
    for operation in operations[:-1]:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```