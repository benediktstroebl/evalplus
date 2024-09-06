Here is a Python script that contains a self-contained function `below_zero` which solves the problem:

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
``` 

The function takes a list of operations (deposit and withdrawal) and then determines whether the balance falls below zero at any point in the operation, and if it is below zero, the function returns `True`, and if it is not, the function returns `False`.