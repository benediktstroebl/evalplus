```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ Checks if any operation in the list will cause a balance below zero.
    return True if any operation in the operations causes a balance below zero, otherwise False is returned.
    """ - operations = operations + [0]
    return below_zero(operations)
    """
# Tests
assert below_zero([1, 2, -4, 5]) == True
assert below_zero([1, 2, -4, 5, 0]) == False
assert below_zero([0, 1, 2, -4, 5]) == False
assert below_zero([]) == False
```