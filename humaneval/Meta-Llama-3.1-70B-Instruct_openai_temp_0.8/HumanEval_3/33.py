```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

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
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([10, -5, 2, -8]))  # True
```