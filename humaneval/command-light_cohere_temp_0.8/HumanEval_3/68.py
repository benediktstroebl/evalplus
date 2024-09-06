```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This script defines a function called below_zero that takes a list of operations as an argument. The function iterates over each operation in the list, and adds the operation to the balance variable. The function returns 'True' if at any point the balance falls below zero, and 'False' otherwise.