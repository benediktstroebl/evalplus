Here's the Python script with the self-contained function below_zero, which solves the problem you described:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([5, 2, 3, 1])
    False
    >>> below_zero([100, -100, 200])
    True
    >>> below_zero([100, 0, 200])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function checks if the current balance falls below zero after processing all operations. The loop iterates over each operation in the list, and accumulates the balance after each operation. The function returns True if the balance is less than zero, and False otherwise.