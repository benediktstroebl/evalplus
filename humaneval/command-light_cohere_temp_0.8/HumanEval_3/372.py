```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([4, -3, -2, -1])
    False
    >>> below_zero([2, 8, 2, 4])
    True
    """
    for op in operations:
        if op < 0:
            return True
    return False
``` 
This function checks each operation in the list, and if it finds an operation that is less than zero, it returns True. If all operations are greater than zero, the function will return False.