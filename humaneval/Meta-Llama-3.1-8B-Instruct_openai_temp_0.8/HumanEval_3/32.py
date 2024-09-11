```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # Return True if the balance falls below 0
    return False  # Return False if the balance never falls below 0

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below 0 at any point, and `False` otherwise. The function initializes the balance to 0, then iterates over the operations, updating the balance and checking if it falls below 0. If it does, the function immediately returns `True`. If the function completes the iteration without the balance falling below 0, it returns `False`. The script also includes test cases to demonstrate the function's behavior.