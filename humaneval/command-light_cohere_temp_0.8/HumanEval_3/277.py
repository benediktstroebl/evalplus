```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ Detects if the balance of the account falls below zero at any point.
    >>> operations = [-4, 5, 1, 2, -3]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([10, 2, -4, 5])
    False
    """
    for x in operations:
        if x < 0:
            return True
    return False
``` 
This function checks the list of operations for each element being less than 0, if found any such number, it will return True. If not, it will return False, which means no negative number operation and the balance is always above 0.