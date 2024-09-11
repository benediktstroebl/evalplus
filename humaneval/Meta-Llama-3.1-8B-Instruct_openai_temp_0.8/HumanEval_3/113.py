```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero

    # Iterate over each operation in the list
    for operation in operations:
        balance += operation  # Update the balance by adding the current operation

        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True

    # If the loop completes without the balance falling below zero, return False
    return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 5, -10, 10]))  # True
print(below_zero([-10, -5, -5, -10, -10]))  # True
print(below_zero([10, 10, 10, 10, 10]))  # False
```