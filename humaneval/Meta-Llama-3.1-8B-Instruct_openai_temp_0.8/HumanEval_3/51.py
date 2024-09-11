```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if at any point the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance with the current operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, immediately return True
    return False  # If the loop completes without the balance falling below 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([5, 5, 5, 5]))  # False
print(below_zero([-1, -2, -3]))  # True
```

This script defines a function `below_zero` that checks if at any point the balance of a bank account falls below zero, given a list of deposit and withdrawal operations. It iterates over the operations, updating the balance and checking if it falls below zero. If it does, the function immediately returns `True`; otherwise, it returns `False`. The test cases demonstrate the function's behavior in various scenarios.