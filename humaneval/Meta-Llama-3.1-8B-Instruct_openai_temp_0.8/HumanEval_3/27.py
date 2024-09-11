```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero after a series of operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Add each operation to the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If the loop completes without finding a balance below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance of the account falls below zero at any point, and `False` otherwise. The function iterates over the operations, updating the balance after each operation, and returns `True` as soon as it finds a balance below zero. If the loop completes without finding a balance below zero, the function returns `False`.