```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance with 0
    for op in operations:
        balance += op  # Update the balance for each operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # Return True as soon as the balance falls below 0
    return False  # If no operation caused the balance to fall below 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input. It keeps track of the current balance by iterating through each operation, adding the operation to the balance, and checking if the balance has fallen below zero. If it has, the function immediately returns `True`. If the function iterates through all operations without the balance falling below zero, it returns `False`. The script includes test cases to demonstrate the function's behavior.