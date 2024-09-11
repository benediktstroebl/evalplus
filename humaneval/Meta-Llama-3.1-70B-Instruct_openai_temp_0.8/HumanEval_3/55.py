```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero


# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([10, 20, 30]))  # False
```