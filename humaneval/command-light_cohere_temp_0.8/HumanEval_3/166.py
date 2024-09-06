Here's the complete Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3, -5])
    False
    >>> below_zero([0, 1, 2, 3])
    False
    >>> below_zero([10, 2, -3, 4])
    True
    """
    balance = 0
    for operation in operations:
        if operation > 0:  # deposit
            balance += operation
        elif operation < 0:  # withdrawal
            return False
    return balance < 0
```
This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It uses a
 balance variable to keep track of the account balance, starting with 0. The function then loops through each operation in the list. If the operation is a positive value (deposit), it adds the value to the balance. If the operation is a negative value (withdraw), it returns False, as the balance would be below zero at this point.