```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point in a list of deposit/withdrawal operations, 
    the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It uses a simple iterative approach to calculate the balance after each operation and returns True as soon as the balance falls below zero. If the balance never falls below zero, it returns False. The example usage demonstrates the function's behavior with different input lists.