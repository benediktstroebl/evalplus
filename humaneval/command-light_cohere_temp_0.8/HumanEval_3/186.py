```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([5, -4, 3, 2, 1])
    False
    >>> below_zero([-1000, -100, -500])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```  The provided code defines a Python function `below_zero` that checks whether the balance of a bank account falls below zero after processing a list of operations. The function uses a balance variable to keep track of the account balance and iterates over each operation in the `operations` list. The final balance is checked against the initial balance of zero.