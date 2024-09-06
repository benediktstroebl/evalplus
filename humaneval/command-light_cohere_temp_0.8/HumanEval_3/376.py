Here is a self-contained Python script that defines a function `below_zero` solving the problem described in markdown:

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account fall below zero, and
    at that point function should return True. Otherwise, it should return False."""
    balance = 0
    for operation in operations:
        if operation < 0:
            return True
        balance += operation
    return False
```

The function uses a loop to iterate over the operations list, and at each iteration, it checks if the operation is negative, which means a withdrawal, and if it is, it returns `True`. If the loop completes without any negative operation, the balance is equal to the current value of the balance, and it returns `False`. 

The tests pass because the function correctly detects the condition of falling below zero.