```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

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


# Example usage
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines a function `below_zero` that takes a list of operations (deposits and withdrawals) and returns `True` if the balance falls below zero at any point, and `False` otherwise. It iterates over the operations, updates the balance, and checks if the balance is less than zero after each operation. If the balance falls below zero, the function immediately returns `True`. If the function finishes iterating over the operations without the balance falling below zero, it returns `False`. The script includes example usage to demonstrate the function's behavior.