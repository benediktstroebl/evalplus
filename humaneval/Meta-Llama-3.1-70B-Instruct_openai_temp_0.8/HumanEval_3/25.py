```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance falls below zero after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Apply each operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True
    return False  # If the function hasn't returned True, the balance never fell below zero


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, 3, -4, 2]))  # False
```