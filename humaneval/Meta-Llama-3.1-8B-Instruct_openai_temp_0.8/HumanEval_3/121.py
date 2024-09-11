```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True if balance falls below zero
    return False  # If no operation causes balance to fall below zero, return False

# Test the function
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

In this script, we initialize a variable `balance` to zero. Then, we iterate over each operation in the `operations` list. For each operation, we update the `balance` by adding the operation. If the `balance` falls below zero at any point, we immediately return `True`. If we complete the iteration without the `balance` falling below zero, we return `False`.