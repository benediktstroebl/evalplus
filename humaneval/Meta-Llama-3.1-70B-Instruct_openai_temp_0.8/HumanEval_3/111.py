```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance as zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance
        if balance < 0:  # Check if balance is less than zero
            return True  # Return True if balance falls below zero
    return False  # Return False if balance never falls below zero

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account. The function iterates over each operation, updates the balance, and checks if the balance falls below zero. If it does, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.