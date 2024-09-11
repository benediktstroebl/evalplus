```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If no negative balance is found, return False


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([5, -10, 3, 7]))  # Expected output: True
print(below_zero([2, 3, 5, 7]))  # Expected output: False
```