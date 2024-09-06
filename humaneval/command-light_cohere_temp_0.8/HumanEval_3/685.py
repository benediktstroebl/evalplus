```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [[-1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [10, -1, 3]
    >>> below_zero(operations)
    False
    """
    balance = 0
    for op in operations:
        if op <= 0:
            return True
        balance += op
    return False
```  The function checks if the balance of the account ever falls below zero, and returns True if it does. If the balance remains non-negative after iterating through all operations, the function returns False.