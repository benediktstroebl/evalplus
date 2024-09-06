Here is a Python script that includes a self-contained function that solves the problem you've described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and 
    at that point function should return True. Otherwise, it should return False. 
    >>>operations
    final balances below zero 
    """
    operations = sorted(set(operations))
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
```