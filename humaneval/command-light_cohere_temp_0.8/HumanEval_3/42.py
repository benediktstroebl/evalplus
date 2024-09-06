```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    operations.append(0)
    operations.remove(0)
    balance = False
    for op in operations:
        if balance < 0 and op > 0:
            return True
        elif balance < 0 and op < 0:
            return True
        elif balance > 0:
            balance = False
    return balance
```