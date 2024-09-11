```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, 3]))  # True
print(below_zero([10, -5, 5, -10, 10]))  # True
```

This script defines a function `below_zero` that takes a list of operations (deposits and withdrawals) as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over the list of operations, updating the balance after each operation and checking if it falls below zero. If it does, the function immediately returns `True`. If the function completes the iteration without finding a negative balance, it returns `False`.