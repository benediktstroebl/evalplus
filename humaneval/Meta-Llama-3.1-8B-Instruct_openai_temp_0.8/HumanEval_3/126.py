```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Add each operation to the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    return False  # If we've iterated over all operations without returning True, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing bank account operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over the operations, updating the balance and checking if it falls below zero. The test cases demonstrate the function's behavior.