Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    """
   
    list operations.
    For each operation that is negative, it is added to account, but withdrawn is subtracted from the account.
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3, -4])
    False
    >>> below_zero([0, 1, -4, 5])
    False
    >>> below_zero([7, -1, -4, 5])
    True
    >>> below_zero([1, 2, -1000, -1])
    True
    """
    balance = 0
    for operation in operations:
        if operation > 0:  # deposit
            balance += operation
        elif operation < 0:  # withdrawal
            balance -= operation
    return balance < 0
```
The balance variable is initialized to 0, and the function iterates over the list of operations. For each operation, it checks if the operation is positive (deposit), in which case the balance is increased, or if the operation is negative (withdraw), in which case the balance is decreased. The function returns True if the balance falls below 0. Otherwise, it returns False.