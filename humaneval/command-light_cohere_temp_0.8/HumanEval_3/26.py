Here's the self-contained Python script with a function below_zero that detects if the balance of the account falls below zero. 

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations
    EXAMPLES
    NOT TESTED
    """
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
```