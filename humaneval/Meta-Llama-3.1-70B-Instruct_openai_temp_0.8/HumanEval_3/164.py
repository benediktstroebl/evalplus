```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero 
    after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True if balance falls below zero
    return False  # Return False if balance never falls below zero

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([1, -2, 3, -4, 5]))  # True
```