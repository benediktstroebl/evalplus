Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([2, 4, -1, 6])
    False
    >>> below_zero([4, -8, 12, -10])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function takes a list of operations and iterates through each one. It adds the balance to the account balance by adding the operation. Then it checks if the balance is less than 0. If so is the, the function returns True, otherwise, it returns False.