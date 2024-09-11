```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance by adding the operation
        if balance < 0:  # If balance falls below 0, return True
            return True
    return False  # If no operation makes balance fall below 0, return False


# Example usage
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It iterates over each operation, updating the balance accordingly. If the balance ever falls below zero, it immediately returns `True`. If no operation causes the balance to fall below zero, it returns `False`. The example usage demonstrates how to call the function with example inputs.