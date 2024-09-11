```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance falls below zero 
    after a series of deposit and withdrawal operations.

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

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([100, -50, -60]))  # True
print(below_zero([-10, 20, 30, 40]))  # True
print(below_zero([10, 20, 30, 40]))  # False
```