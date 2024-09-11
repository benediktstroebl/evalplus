```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero,
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance as 0
    for operation in operations:
        balance += operation  # Update the balance for each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # If no operation has caused the balance to fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we use a simple iterative approach to calculate the balance after each operation. If the balance falls below zero at any point, we immediately return True. If we finish all operations without the balance falling below zero, we return False.