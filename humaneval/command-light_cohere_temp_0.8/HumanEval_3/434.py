Here's the self-contained Python script with the `below_zero` function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    # Initialize a flag to store if balance ever falls below zero
    balance_flag = False
    
    # Iterate through operations
    for operation in operations:
        if balance_flag and operation < 0:
            return True
        balance -= operation
        balance_flag = balance <= 0
    
    return balance_flag
```
This function, `below_zero`, takes a list of operations as input and returns a boolean value indicating whether the balance of the account ever falls below zero. It iterates through operations and checks if the balance falls below zero at any point. The function then returns `True` if this is the case, and `False` otherwise.