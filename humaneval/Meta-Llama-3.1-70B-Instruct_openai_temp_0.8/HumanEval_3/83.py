```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
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
print(below_zero([5, -10, 3, 2]))  # True
print(below_zero([1, 1, 1, 1]))  # False
```

This script defines a function `below_zero` that takes a list of operations (deposits and withdrawals) and checks if the balance ever falls below zero. It iterates over the operations, adding each one to the balance. If the balance becomes negative, the function immediately returns `True`. If the function finishes iterating over the operations without the balance falling below zero, it returns `False`. The script includes several example use cases to demonstrate the function's behavior.