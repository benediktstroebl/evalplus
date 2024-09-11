```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Update balance
        if balance < 0:  # If balance falls below zero
            return True  # Return True
    return False  # If no operation causes balance to fall below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 1, 1, 1]))  # False
```