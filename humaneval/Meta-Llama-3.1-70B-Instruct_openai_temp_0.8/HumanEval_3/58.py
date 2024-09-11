```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance falls below zero after a series of deposit and withdrawal operations.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If no operation makes the balance fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, 5, -15]))  # True
```