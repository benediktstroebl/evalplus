```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True immediately
    return False  # If the function hasn't returned True by now, the balance never fell below zero

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It iterates through each operation, updating the balance and checking if it's below zero after each update. If the balance ever falls below zero, the function returns `True` immediately; otherwise, it returns `False` after processing all operations. The script also includes example usage to demonstrate how to use the function.