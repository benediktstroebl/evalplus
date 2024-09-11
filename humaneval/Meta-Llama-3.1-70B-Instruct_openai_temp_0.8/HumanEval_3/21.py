```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point
    given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit and withdrawal operations.
            Positive numbers represent deposits and negative numbers represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If we've iterated over all operations and the balance is never below zero, return False


# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([1, 2, 3, 4]))  # False
```