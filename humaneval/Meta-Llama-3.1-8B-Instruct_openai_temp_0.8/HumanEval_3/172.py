```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance by adding the operation
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True as soon as balance falls below zero
    return False  # If no operation caused balance to fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 6, -3]))  # True
print(below_zero([0, 0, 0, 0]))  # False
```

This script uses a simple iterative approach to track the balance and check if it falls below zero at any point. The `for` loop iterates over the operations, updating the balance by adding each operation. As soon as the balance falls below zero, the function returns `True`. If no operation causes the balance to fall below zero, the function returns `False` after iterating over all operations.