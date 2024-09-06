Here is a Python script that includes a self-contained function that solves the problem you provided:
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
    >>> below_zero([0, -1, 3])
    False
    >>> below_zero([1000, -2000, 3000])
    True
    """
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
    return balance < 0
```
The function below_zero takes a list of operations and returns a boolean value indicating whether the balance falls below zero at any point in the operations. The function loops through each operation and adds it to the balance. If the operation is greater than 0, the balance is increased by the operation. If the balance is greater than 0 after the loop, the function returns False, indicating that the balance is still positive. If the balance is less than 0, the function returns True, indicating that the balance is less than 0.