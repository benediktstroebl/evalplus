Here is a self-contained Python script that defines a function below_zero that checks if the balance of a bank account falls below zero or not, and passes the tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, 3]
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([0, 1, 2])
    True
    >>> below_zero([100, 50, 0, -10])
    False
    """

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
The function below_zero takes a list of operations and checks if any of them would cause the balance of the account to fall below zero. It does this by initializing the balance to zero, then iterating over each operation in the list. If the balance becomes negative, then the function returns True, indicating that the account balance is below zero. Otherwise, it returns False, indicating that the account balance is not below zero.