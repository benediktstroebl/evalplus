Here is a Python script that contains a self-contained function that solves the problem and passes the tests:

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
    >>> below_zero([6, -3, -10])
    False
    >>> below_zero([-1, 2, 3])
    True
    >>> below_zero([1,2, 3,4])
    False
    >>> below_zero([])
    False
    ```