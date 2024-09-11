```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account goes below zero at any point
    after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive integers) and withdrawal (negative integers) operations.

    Returns:
        bool: True if the balance goes below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    return False  # If the function hasn't returned True after all operations, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a `balance` variable to zero and then iterates over each operation in the list, updating the balance accordingly. If the balance ever goes below zero, the function returns `True`. If the function finishes iterating over all operations without the balance going below zero, it returns `False`.