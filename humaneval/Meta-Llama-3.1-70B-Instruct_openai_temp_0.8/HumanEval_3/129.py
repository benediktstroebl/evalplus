```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account balance falls below zero after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
print(below_zero([1, -2, 3, -4, 5]))  # Output: True
print(below_zero([10, 20, 30]))  # Output: False
```