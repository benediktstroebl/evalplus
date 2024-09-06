Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with 
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    balance = 0
    for op in operations:
        if op < 0:
            balance -= op
        elif balance < 0:
            return True
    return False
```
The function uses a loop to iterate through each operation in the list. The function performs operations and checks the balance at every step. If it detects that the balance falls below zero, it returns True. Otherwise, it returns False.