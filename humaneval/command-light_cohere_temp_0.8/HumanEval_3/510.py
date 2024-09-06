Here is a self-contained Python script that defines a function below_zero that solves the problem:
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
    >>> below_zero([0, 1, 2])
    False
    >>> below_zero([9, 1, 2])
    True
    >>> below_zero([100, 1, 2])
    False
    >>> below_zero([100, -100, 1])
    False
    >>> below_zero([1, 2, 3, 4])
    False
    """

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```
This function takes a list of operations as input and returns a boolean indicating whether the balance of the account falls below zero at any point. The function uses a balance variable to keep track of the current balance. The function iterates through the balance variable and adds or subtracts the corresponding operation in the operations list. If the current balance is greater than 0, the function returns False, indicating that the balance is not below zero. If the balance is less than 0, the function returns True, indicating that the balance is below zero.