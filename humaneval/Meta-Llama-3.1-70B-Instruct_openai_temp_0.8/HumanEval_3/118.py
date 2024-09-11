```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account balance falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the bank account balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True immediately
    return False  # If the function hasn't returned True, the balance never fell below zero

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 3, -15, 20]))  # True
print(below_zero([5, 10, 20, 30]))  # False
```