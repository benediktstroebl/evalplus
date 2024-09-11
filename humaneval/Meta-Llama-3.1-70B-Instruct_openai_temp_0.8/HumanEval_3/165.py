```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
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
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, 3, -8, 4]))  # True
print(below_zero([10, 5, 3, 8, 4]))  # False
```

This script defines a function `below_zero` that iterates over a list of operations, updating a running balance. If the balance ever falls below zero, the function immediately returns `True`. If the function finishes iterating over the operations without the balance falling below zero, it returns `False`. The script includes several example use cases to demonstrate the function's behavior.