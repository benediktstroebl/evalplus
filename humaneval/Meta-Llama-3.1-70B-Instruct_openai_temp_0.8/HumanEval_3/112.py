```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If we've checked all operations and the balance was never below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([-1, 2, 3]))  # Expected output: True
print(below_zero([1, -2, 3, -4]))  # Expected output: True
print(below_zero([10, -5, 5, -10, 10]))  # Expected output: True
```