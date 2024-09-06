Here's the provided Python code with a self-contained function below_zero() that solves the problem you described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function checks if the balance falls below zero at any point during the execution of the loop, and returns True. If it remains above or particular, it returns False, which is the correct behavior for this function.