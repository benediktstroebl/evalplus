```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point
    after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.
        Positive integers represent deposits, and negative integers represent withdrawals.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True immediately
    return False  # If we've iterated over all operations without returning, the balance never fell below zero

# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -10]))  # True
print(below_zero([-1, 5, 10]))  # True
print(below_zero([10, 5, -3]))  # False
```