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
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if it does
    
    return False  # Return False if the loop completes without the balance falling below zero


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing bank account operations and returns a boolean indicating whether the balance falls below zero at any point. It initializes a balance variable to zero, iterates over each operation, and updates the balance accordingly. If the balance falls below zero, it immediately returns True. If the loop completes without the balance falling below zero, it returns False. The script also includes example usage.