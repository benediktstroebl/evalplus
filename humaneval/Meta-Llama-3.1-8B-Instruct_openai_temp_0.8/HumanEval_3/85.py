```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        # Apply each operation to the balance
        balance += operation
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    # If we've checked all operations and the balance never fell below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script uses a simple loop to apply each operation to the balance. As soon as the balance falls below zero, it immediately returns `True`. If it checks all operations without the balance falling below zero, it returns `False`.