Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, 3]
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
``` 
This script defines a function `below_zero` that takes a list of operations as input. The function initializes a balance of 0 and then iterates over each operation in the input list. 

Finally, it checks if the balance is less than 0 and returns the result accordingly.