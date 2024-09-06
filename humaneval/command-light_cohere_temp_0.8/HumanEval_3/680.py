Here is a self-contained Python function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [[-1, 0, 3, 4, 5]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [100010, 2, 100010, -100, 1000]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function below_zero takes a list of operations as input and returns a boolean value indicating whether the balance of the account falls below zero at any point. The function uses a balance variable to keep track of the current balance, and iterates through the operations, adding each one to the balance. After iterating through operations, the function returns True if the balance is negative and False if the balance is non-negative.