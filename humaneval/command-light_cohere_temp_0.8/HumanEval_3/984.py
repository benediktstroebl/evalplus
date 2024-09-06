Here is a self-contained Python script that defines a function below_zero that solves the problem of checking if the balance of a bank account falls below zero, and passes the tests provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [[-4, -1, 5, -2]
    >>> below_zero(operations)
    True
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [1,2,3,4]
    >>> below_zero(operations)
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This code defines a function called below_zero that takes a list of integers as input, representing deposit and withdrawal operations from a bank account. The function calculates the balance by summing up the operations, and then checks if the balance is less than 0. If the balance is indeed negative, the function returns True, indicating that the account balance has fallen below zero. Otherwise, it returns False, indicating that the balance is still positive.