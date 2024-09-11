### Bank Account Balance Tracker
#### Script to detect if bank account balance falls below zero after a series of operations

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of the account falls below zero.

    Args:
    operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the account balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True immediately if the balance goes below zero
    return False  # If the loop completes without the balance going below zero, return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([100, -50, -20, -20]))  # True
```

This script uses a simple iterative approach to track the account balance after each operation. It initializes the balance to zero and updates it after each operation. As soon as the balance falls below zero, it immediately returns True. If the loop completes without the balance going below zero, it returns False.