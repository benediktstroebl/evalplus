Here's the self-contained Python script with the function below_zero that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    balance = 0
    for op in operations:
        if op > 0:
            balance += op
        elif op < 0:
            return False
    return balance < 0
```
The function takes a list of operations as input and iterates through each operation in the list. After iterating through through operations, it adds the operation to the balance. It checks if the balance becomes less than 0 and returns True if it is.