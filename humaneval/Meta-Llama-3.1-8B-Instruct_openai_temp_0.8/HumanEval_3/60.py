```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of the account falls below zero.

    Args:
    operations (List[int]): A list of deposit (positive value) and withdrawal (negative value) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, immediately return True
    return False  # If no operation caused the balance to fall below zero, return False

# Example use cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It iterates over each operation, updating the balance, and checks if the balance falls below zero. If it does, it returns `True`; otherwise, it returns `False`.