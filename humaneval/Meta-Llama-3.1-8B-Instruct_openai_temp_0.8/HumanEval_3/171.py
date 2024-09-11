```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance.
    Your task is to detect if at any point the balance of account falls below zero, and at that point function should return True.
    Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero


# Test the function
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

In this script, we initialize a variable `balance` to zero and iterate over the list of operations. After each operation, we update the `balance` by adding the current operation. We then check if the `balance` is less than zero. If it is, we immediately return `True` to indicate that the balance fell below zero at some point. If we finish iterating over all operations without the balance falling below zero, we return `False`.