```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        # Check if the balance falls below zero after each operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -3, -2]))  # True
print(below_zero([]))  # False
```

This script defines a function `below_zero` that iterates through a list of operations (deposits and withdrawals) and checks if the balance falls below zero at any point. It starts with a balance of zero and updates it after each operation. If the balance falls below zero, it immediately returns `True`. If it iterates through all operations without the balance falling below zero, it returns `False`.