```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account falls below zero balance after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.

    """
    balance = 0  # Initialize the account balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the operation amount
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the function hasn't returned yet, the balance never fell below zero

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 2, 3, -10]))  # True
print(below_zero([10, 2, 3]))  # False
```