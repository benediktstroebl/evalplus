Here is a self-contained Python script that solves the problem:
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
    >>> below_zero([1, 2, 3, -5])
    True
    >>> below_zero([3, 2, -5])
    False
    >>> below_zero([5, -3, -5])
    False
    >>> below_zero([-3, -2, -5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function takes a list of operations (deposit and withdrawal) as input. It initializes a balance to zero and then iterates over each operation in the list. By adding the operator, it updates the balance. The function returns True if at any point, the balance becomes less than zero, indicating that the account has fallen below zero.