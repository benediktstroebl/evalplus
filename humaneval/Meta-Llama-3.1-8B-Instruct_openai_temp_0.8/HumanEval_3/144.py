### Python Script to Check if Bank Account Falls Below Zero
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the bank account balance falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
print(below_zero([10, -5, 2, -3, 7]))  # Output: False
print(below_zero([10, -15, 2, -3, 7]))  # Output: True
```