```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If we've iterated over all operations without the balance going below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```

This script defines a function `below_zero` that takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise. It initializes the balance to zero, then iterates over each operation, adding it to the balance. If the balance ever goes below zero, it immediately returns `True`. If it iterates over all operations without the balance going below zero, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.