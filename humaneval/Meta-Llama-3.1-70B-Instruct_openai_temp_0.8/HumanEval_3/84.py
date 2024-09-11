```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a list of deposit and withdrawal operations causes a bank account to fall below zero balance.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Apply the operation to the balance
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If so, immediately return True
    return False  # If no operations caused the balance to fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -15, 5]))  # True
print(below_zero([-5, 10, -3, 8]))  # True
print(below_zero([10, 20, 30]))  # False
```