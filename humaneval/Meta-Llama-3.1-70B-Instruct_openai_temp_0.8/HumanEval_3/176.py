```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations. Positive values represent deposits, and negative values represent withdrawals.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the account balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True immediately
    return False  # If the loop completes without finding a negative balance, return False

# Example usage
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```