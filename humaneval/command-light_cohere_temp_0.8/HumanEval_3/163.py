Here is a self-contained Python script that defines a function `below_zero` that solves the problem you provided: 
```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    """
>>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This function takes a list of operations as input and iterates through each operation in the list. It adds the balance by adding the operation to the balance variable.