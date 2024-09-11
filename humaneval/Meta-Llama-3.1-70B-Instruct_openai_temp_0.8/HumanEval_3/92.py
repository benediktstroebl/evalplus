```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks a list of deposit and withdrawal operations on a bank account 
    that starts with zero balance. It returns True if at any point the balance of the 
    account falls below zero, otherwise it returns False.

    Args:
        operations (List[int]): A list of integers representing deposit (positive) and 
            withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance is below zero
    return False  # Return False if the balance never falls below zero


# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```