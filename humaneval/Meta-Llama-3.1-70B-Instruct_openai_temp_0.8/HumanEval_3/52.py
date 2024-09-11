```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize account balance to zero
    for operation in operations:
        balance += operation  # Update balance after each operation
        if balance < 0:  # Check if balance falls below zero
            return True  # If yes, return True
    return False  # If no, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([1, 2, 3, 4]))  # False
```