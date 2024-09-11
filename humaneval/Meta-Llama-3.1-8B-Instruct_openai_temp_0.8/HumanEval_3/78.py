```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If no operation caused the balance to fall below zero, return False


# Example usage
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines a function `below_zero` that takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes a `balance` variable to zero, iterates over each operation, updates the balance, and checks if it falls below zero. If it does, the function returns `True` immediately. If no operation causes the balance to fall below zero, the function returns `False`.