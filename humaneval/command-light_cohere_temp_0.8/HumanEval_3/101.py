```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [-4, 5]
    # using list comprehension to check if any value in operations is negative
    return any(x < 0 for x in operations)
``` 
This function is self-contained, and it efficiently checks if the operations in the list will cause the balance to fall below zero.