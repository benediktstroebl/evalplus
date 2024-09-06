```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0]
    >>> below_zero(operations)
    True
    >>> operations = [100, 0, -1]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, 3]
    >>> below_zero(operations)
    True
    """
    operations.remove(0)  # Remove the starting balance of 0
    for i, o in enumerate(operations):
        if o < 0:
            return True
    return False
```