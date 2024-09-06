```Python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 2, -4, 5])
    False
    >>> below_zero([9, 2, -4, 5])
    True
    >>> below_zero([1,2,3,4,5,6,7])
    False
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```  The above code checks if the balance of the account ever falls below zero. It does this by iterating through the operations and checking if the balance ever becomes negative.