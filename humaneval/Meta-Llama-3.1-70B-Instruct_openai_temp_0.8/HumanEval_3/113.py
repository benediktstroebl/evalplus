```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the function hasn't returned True after all operations, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([-1, -2, -3]))  # Expected output: True
print(below_zero([10, -5, 3, -7, 1]))  # Expected output: True
```

This script defines the `below_zero` function as specified, and includes test cases to verify its correctness. The function iterates over each operation in the input list, updating the balance accordingly. As soon as the balance falls below zero, the function returns `True`. If the function completes all operations without the balance falling below zero, it returns `False`.