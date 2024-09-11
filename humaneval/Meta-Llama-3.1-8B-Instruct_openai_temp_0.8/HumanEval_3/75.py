```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance is negative
            return True  # Return True immediately
    return False  # If we reach this point, the balance never fell below zero

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```