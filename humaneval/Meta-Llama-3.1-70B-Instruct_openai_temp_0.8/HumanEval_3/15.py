```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero,
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: Whether the balance falls below zero at any point.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that iterates over a list of operations. For each operation, it updates the balance and checks if it's below zero. If it is, it immediately returns `True`. If it iterates over the entire list without the balance falling below zero, it returns `False`.