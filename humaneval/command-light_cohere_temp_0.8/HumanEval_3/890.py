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
    >>> below_zero([0, 2, 3])
    False
    >>> below_zero([-1, -2, -3, -4])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The code defines a function `below_zero` that takes a list of operations and checks if the balance of the account ever falls below zero. The function iterates through each operation in the list, and adds it to the current balance. If at any point the thus, the balance reaches negative, then the function will return `True`, indicating that the balance has fallen below zero. Otherwise, it returns `False` and the balance remains non-negative.