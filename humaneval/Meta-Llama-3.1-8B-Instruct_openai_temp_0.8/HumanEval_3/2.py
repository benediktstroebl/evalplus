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
    bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add operation to the balance
        if balance < 0:  # Check if balance is below zero
            return True  # Return True if balance is below zero
    return False  # If no operation caused balance to be below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a balance to zero and iterates over each operation, adding it to the balance. It checks after each operation if the balance is below zero, and if so, it immediately returns `True`. If no operation causes the balance to be below zero, it returns `False`.