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
    >>> below_zero([3, 2, -4, 5])
    False
    >>> below_zero([0, 4, -5])
    True
    >>> below_zero([1, 2, 3, -4])
    True
    >>> below_zero([100, -50, 3, -2])
    False
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This function below_zero takes a list of operations as input and returns a boolean value. It iterates over each operations in the list, adding the value of each operation to the balance. Finally, it returns True if the balance is less than zero, indicating that the account has fallen below zero.