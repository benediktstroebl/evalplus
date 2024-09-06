```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point, function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1,2,3,4,5])
    False
    >>> below_zero([9, 2, -3, 1])
    True
    """
    # Following recursive implementation
    def check(balance, operation):
        if balance < 0:
            return True
        if balance == 0:
            return False
        elif operation > 0:  # deposit case
            balance += operation
            return check(balance, operation)
        else:  # withdrawal case
            balance -= operation
            return check(balance, operation)
    return check(0, 0)  # base case
```
The function below_zero accepts a list of operations as input. It then uses a recursive function check to determine if the balance falls below zero. The check function, in turn, calls itself recursively to determine if the balance is above or below zero after performing the operation. The base case is when there are no operations, and the balance is zero, it returns False. Otherwise, it returns True if there are operations.