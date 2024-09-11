```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero,
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the function hasn't returned True by now, it means the balance never fell below zero


# Example usage
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-10, -20, -30]))  # True
print(below_zero([10, 20, 30]))  # False
```

This script uses a simple loop to iterate over each operation in the list. It keeps track of the current balance and checks if it falls below zero. If it does, the function returns True immediately. If the function finishes iterating over all operations without returning True, it means the balance never fell below zero, so it returns False.