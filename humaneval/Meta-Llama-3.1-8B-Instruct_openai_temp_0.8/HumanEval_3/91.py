```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, 
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of operations (deposit or withdrawal) on a bank account.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True if balance falls below zero
    return False  # If no operation causes balance to fall below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if at any point the balance falls below zero, and `False` otherwise. The function initializes the balance to zero, iterates over the operations, and updates the balance accordingly. If the balance falls below zero, it immediately returns `True`. If it iterates over all operations without finding a balance below zero, it returns `False`. The script includes two test cases to verify the correctness of the function.