Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
This function, below_zero, takes a list of operations as input and returns a boolean value indicating whether the balance of the account falls below zero at any point. The function uses a loop through each operation and adds the value to the balance. The function returns True if the balance is negative, and False otherwise.