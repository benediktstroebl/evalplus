```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account balance falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance for each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If no operation resulted in a balance below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It uses a simple iterative approach to update the balance for each operation and checks if it falls below zero. The test cases at the end demonstrate the function's correctness.