```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of deposit and withdrawal operations on a bank account and returns True if 
    the balance ever falls below zero, False otherwise.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance ever falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If the loop completes without the balance going below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance ever falls below zero. It uses a simple loop to iterate over the operations, updating the balance and checking if it goes below zero after each operation. If it does, the function returns True immediately. If the loop completes without the balance going below zero, the function returns False.