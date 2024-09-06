```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([3, 2, -1, 1, -5])
    False
    >>> below_zero([0, 1, 2])
    False
    >>> below_zero([9, -8, -10])
    True
    """
    balance = 0
    for op in operations:
        if op > 0:
            balance += op
        elif op < 0:
            return True
    return False
```  This Python code defines a function named below_zero that checks a list of operations for a bank account to determine if the balance falls below zero. The function initializes a balance to zero, and then iterates through each operation in the operations list. If the operation is greater than zero, it adds the operation to the balance, which could potentially make the balance below zero. If the operation is negative and greater than zero, it does nothing and returns False. If the operation is smaller than zero, it returns True, indicating that the balance is below zero.