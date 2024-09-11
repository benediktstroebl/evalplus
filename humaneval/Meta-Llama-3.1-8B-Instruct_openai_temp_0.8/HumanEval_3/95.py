```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance based on the operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, return True immediately
    return False  # If we've iterated over all operations without returning, the balance never fell below 0

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It uses a simple loop to iterate over the operations and update the balance accordingly. If the balance falls below zero, it returns `True` immediately; otherwise, it returns `False` at the end of the loop.