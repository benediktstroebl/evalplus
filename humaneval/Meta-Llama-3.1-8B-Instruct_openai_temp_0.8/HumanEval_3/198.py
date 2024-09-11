```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero,
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations

    Returns:
        bool: True if balance falls below zero, False otherwise
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:
        balance += operation  # Add operation to balance
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True as soon as balance falls below zero
    return False  # Return False if balance never falls below zero


# Test the function
print(below_zero([1, 2, 3]))  # Should return False
print(below_zero([1, 2, -4, 5]))  # Should return True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance ever falls below zero, and `False` otherwise. It initializes the balance to zero and then iterates over the list of operations, adding each operation to the balance. As soon as the balance falls below zero, it returns `True`. If the function finishes iterating over the list without the balance falling below zero, it returns `False`.