```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the current operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If we've iterated over all operations and haven't fallen below zero, return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance ever falls below zero, and `False` otherwise. It uses a simple loop to calculate the balance after each operation and checks if it has fallen below zero.