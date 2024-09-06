```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations) 
    True
    >>> operations = [1, 2, 3]
    >>> below_zero(operations) 
    False
    """
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            break
    return balance < 0
``` 
The function checks if the balance falls below zero. If so, it returns True, and False otherwise.