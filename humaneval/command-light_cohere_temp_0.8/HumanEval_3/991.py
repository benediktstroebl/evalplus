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
    >>> below_zero([5, -4, 1, 2])
    False
    >>> below_zero([0, -3, 4, -2])
    True
    >>> below_zero([100, 50, 20, 2])
    False
    """
    balance = 0
    for num in operations:
        balance += num
    return balance < 0
```
Do you have a function below_zero that takes a list of operations and returns a boolean indicating whether the balance of the account goes below zero after processing those operations. 
This function calculates the balance and checks if it becomes negative.