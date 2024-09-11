```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point
    given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit and withdrawal operations.
            Positive numbers are deposits and negative numbers are withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
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
print(below_zero([10, -5, -7]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([0, 0, 0]))  # False
```