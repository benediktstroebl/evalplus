```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # If no operation causes the balance to fall below zero, return False

# Test the function
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. It initializes the balance to zero, iterates over the operations, updates the balance, and checks if the balance falls below zero. If it does, it returns `True`. After iterating over all operations, it returns `False` to indicate that no operation caused the balance to fall below zero. The script includes test cases to demonstrate the function's behavior.