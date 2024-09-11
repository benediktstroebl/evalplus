```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account's balance falls below zero at any point
    given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit and withdrawal operations.
                             Positive values represent deposits and negative values represent withdrawals.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over each operation, updates the balance, and checks if the balance falls below zero. If it does, the function returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.