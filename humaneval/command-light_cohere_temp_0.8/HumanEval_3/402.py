Here is a self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and 
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 1, 2])
    False
    >>> below_zero([1, 2, -2, 3])
    True
    >>> below_zero([10, -5, 20])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function takes a list of operations and loops through the list. It then maintains a balance of the account and adds each operation in the list. Finally, it checks if the balance is less than zero and returns the result accordingly.