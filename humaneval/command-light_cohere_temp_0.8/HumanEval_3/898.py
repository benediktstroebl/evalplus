```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Check if any operation in the list will cause a balance below zero.
    """
    test case:
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    for x in operations:
        if x <= 0:
            return True
    return False
```