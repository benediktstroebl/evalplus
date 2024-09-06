```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ Detects whether the balance of the account ever falls below zero by iterating through the list of deposit and withdrawal operations.
    Operations are: List of integers, with the first element being the deposit and the last element being the withdrawal.
    Balance: Initial balance set to zero.
    Deposited by account is the first element in the list, and withdrawal is the last element in the list.
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, -2, -4, 5])
    False
    >>> below_zero([5, 1, -4, -2, 3])
    True
    >>> below_zero([0, 0, -4, 5])
    False
    """

balance = 0

for operation in operations:
    if operation > 0:
        balance += operation
    elif operation < 0:
        balance -= operation
    else:
        return True

return balance <= 0
```