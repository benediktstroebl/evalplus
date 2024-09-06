Here's the improved Python script with self-contained function below_zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [[-4, 5, 1, 2]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([4, 5, -1, 2])
    False
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
The above-mentioned code will check the operations on a bank account and determine whether the balance falls below zero. It will return True if this condition is met, and False if it is not.

The function uses the balance variable to keep track of the current balance and adds each operation to the balance. The function returns True if the balance is less than 0, indicating that the account balance has fallen below zero.