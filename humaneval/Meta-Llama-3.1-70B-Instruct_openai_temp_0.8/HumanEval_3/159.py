```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if a bank account's balance falls below zero given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
```