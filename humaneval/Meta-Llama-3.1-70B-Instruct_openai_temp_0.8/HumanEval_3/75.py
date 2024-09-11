```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if it does
    return False  # Return False if the balance never falls below zero


# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([10, -5, 3, -8]))  # True
```