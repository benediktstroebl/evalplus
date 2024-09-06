```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    Checks whether the operations result in a balance below zero.
    Operations are given as a list of deposit and withdrawal operations on a bank account that starts with zero balance. 
    Args: 
    - operations: list of integers. 
    Returns: True if the balance becomes negative at any point, otherwise False.
    """
    balance = 0
    for x in operations:
        balance += x
        if balance < 0:
            return True
    return False
```