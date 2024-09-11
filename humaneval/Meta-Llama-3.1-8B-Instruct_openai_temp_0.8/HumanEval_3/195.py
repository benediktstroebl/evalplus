```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        # If the balance is negative, return True immediately
        if balance < 0:
            return True
    # If we've iterated through all operations and haven't returned True, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 2, -3]))  # True
print(below_zero([10, 5, 2, 3]))  # False
```

This Python script defines a function `below_zero` that takes a list of integer operations as input and returns a boolean indicating whether the balance falls below zero at any point. The function initializes a balance variable to 0 and then iterates through the operations. For each operation, it adds the operation to the balance and checks if the balance is negative. If the balance is negative, it returns `True` immediately. If it iterates through all operations without returning `True`, it returns `False`.