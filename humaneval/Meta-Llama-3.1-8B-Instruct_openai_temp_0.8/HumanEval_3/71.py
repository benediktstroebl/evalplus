```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance with the current operation
        if balance < 0:  # Check if balance falls below zero
            return True  # If balance falls below zero, return True
    return False  # If no operation causes balance to fall below zero, return False

# Example usage
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. It initializes the balance to zero and iterates over each operation, updating the balance and checking if it falls below zero. If it does, it returns `True`. If no operation causes the balance to fall below zero, it returns `False`.