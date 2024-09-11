```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If we've iterated over all operations without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines a function `below_zero` that takes a list of integer operations and returns a boolean indicating whether the balance falls below zero at any point. The function uses a simple iterative approach to simulate the operations and track the balance. If the balance falls below zero, the function returns `True` immediately; otherwise, it returns `False` after iterating over all operations. The script includes test cases to verify the function's correctness.