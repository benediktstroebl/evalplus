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
    balance = 0  # Initialize the balance to zero

    for operation in operations:
        balance += operation  # Update the balance after each operation

        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True immediately if the balance falls below zero

    return False  # If the loop completes without finding a negative balance, return False


# Test cases
if below_zero([1, 2, 3]):
    print("Expected False, got True")
else:
    print("Test case 1 passed")

if below_zero([1, 2, -4, 5]):
    print("Expected True, got False")
else:
    print("Test case 2 passed")
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It uses a loop to update the balance after each operation and checks if the balance falls below zero. If it does, it returns `True` immediately. If the loop completes without finding a negative balance, it returns `False`.