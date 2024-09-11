```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([5, -10, 3, 6]))  # True
print(below_zero([5, 2, 3, 1]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a `balance` variable to 0 and then iterates over the operations, adding each one to the balance. If the balance ever falls below 0, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below 0, it returns `False`.

The script includes several example use cases to demonstrate the function's behavior.