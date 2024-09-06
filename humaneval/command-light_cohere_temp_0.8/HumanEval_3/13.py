Here is a self-contained Python script that defines a function `below_zero` to solve the problem you have described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([6, -10, -1, -20])
    False
    >>> below_zero([0, 0, 0, 0])
    False
    >>> below_zero([10, -10, 0, 0])
    True
    """

def below_zero(operations):
    operations = [op for op in operations if op <= 0]
    return operations
```

This script defines a function `below_zero` that takes a list of operations as input. The operations are filtered to only include numbers that are less than zero, and the function returns True if there are any operations less than zero in the list, and False otherwise.

This script is a self-contained solution to the problem you have described. It is more efficient and easier to maintain and test compared to requiring additional dependencies.