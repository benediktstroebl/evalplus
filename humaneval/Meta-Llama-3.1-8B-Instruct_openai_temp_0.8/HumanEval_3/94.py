### Below Zero Balance Detection Script
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations. Positive values represent deposits, while negative values represent withdrawals.

    Returns:
        bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance with each operation
        if balance < 0:  # Check if the balance is below zero
            return True  # Return True if the balance is below zero
    return False  # Return False if the balance never falls below zero

# Example usage
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```
This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance of the account falls below zero at any point. The function initializes the balance to zero, iterates over the operations, and checks if the balance is below zero after each operation. If the balance is below zero, the function returns `True` immediately; otherwise, it returns `False` after iterating over all operations.