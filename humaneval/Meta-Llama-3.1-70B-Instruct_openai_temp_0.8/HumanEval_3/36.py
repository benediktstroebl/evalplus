```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detects if the balance of an account falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit and withdrawal operations.
                             Positive integers represent deposits, while negative integers represent withdrawals.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the account balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the operation amount
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If it has, return True immediately
    return False  # If we've iterated over all operations without the balance falling below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, 3, -2, 1]))  # False
```