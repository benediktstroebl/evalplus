```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If the balance never falls below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 2, 3, -10]))  # True
print(below_zero([10, 5, 3]))  # False
```