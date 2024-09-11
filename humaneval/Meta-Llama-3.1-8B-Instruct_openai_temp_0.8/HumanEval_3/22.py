```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point given a list of deposits and withdrawals.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero

    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If it has, immediately return True

    return False  # If the loop completes without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of integers representing bank account operations and returns a boolean indicating whether the balance falls below zero at any point. The function iterates over each operation, updating the balance and checking if it falls below zero. If it does, the function immediately returns `True`; otherwise, it returns `False` after completing all operations. The script includes test cases to demonstrate the function's behavior.