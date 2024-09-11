```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of deposit and withdrawal operations on a bank account that starts with zero balance.
    It detects if at any point the balance of the account falls below zero, and at that point it returns True.
    Otherwise, it returns False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the loop completes without finding a negative balance, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the account balance falls below zero at any point. The function initializes the balance to zero and iterates over each operation, updating the balance and checking for a negative balance after each operation. If a negative balance is found, the function returns True immediately. If the loop completes without finding a negative balance, the function returns False.