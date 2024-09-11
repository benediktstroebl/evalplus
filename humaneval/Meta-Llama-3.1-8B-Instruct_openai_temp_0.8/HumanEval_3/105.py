```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. This function detects if at any point the balance of account falls below zero,
    and at that point it returns True. Otherwise it returns False.

    Args:
        operations (List[int]): A list of deposit (positive value) and withdrawal (negative value) operations.

    Returns:
        bool: True if the account balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize account balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add/withdraw the operation amount from the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if balance falls below zero
    return False  # Return False if no operation caused the balance to fall below zero


# Example usage
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```