Here is a Python script that contains a self-contained function that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for operation in operations:
        if operation < 0:
            return True
        balance += operation
    return False
``` 
This function takes a list of operations and iterates through the list. The function checks if the balance falls below zero, and if so, it returns True. Otherwise, it returns False. 

This self-contained solution effectively solves the problem you provided.