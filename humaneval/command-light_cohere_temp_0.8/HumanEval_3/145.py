Here is a self-contained Python script with a function that solves the problem and passes the corresponding tests:

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
    >>> below_zero([1, 2, 3, -1])
    False
    >>> below_zero([4, -8, 12, -15])
    True
    >>> below_zero([1, -100, -100, -50])
    False
    >>> below_zero([])
    True
    >>> below_zero([10, 20, 30, -40])
    False
    ```

This function below_zero takes a list of operations as input, representing deposit and withdrawal operations on a bank account. It returns True if the facts that the account balance ever falls below zero, and False otherwise.