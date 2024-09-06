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
    >>> below_zero([0, 2, 3, 4])
    False
    >>> below_zero([1000, 2, 3, -4])
    True
    >>> below_zero([1, 2, 3, -10])
    False
    """
    operations = set(operations) # Convert the list into a set to remove duplicates
    for op in operations:
        if op < 0:
            return True
    return False
``` 
This function takes a list of operations, which may include both deposits and withdrawals, and returns a boolean indicating whether the account balance fell below zero at any point during the operations.