```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of operations (deposit or withdrawal) on a bank account and returns
    True if the balance ever falls below zero, False otherwise.

    Args:
        operations (List[int]): A list of deposit (positive integer) or withdrawal (negative integer) operations.

    Returns:
        bool: True if the balance ever falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero

    for operation in operations:
        balance += operation  # Update the balance with each operation

        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True

    # If we've iterated through all operations without the balance falling below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines the `below_zero` function, which takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates through the operations, updating the balance with each operation, and returns `True` as soon as the balance falls below zero. If the function completes the iteration without finding the balance below zero, it returns `False`. The script also includes example usage of the `below_zero` function.