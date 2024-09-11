```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if the balance of a bank account falls below zero at any point.

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

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3]))  # True
print(below_zero([1, 2, 3, 4]))  # False
```

This Python script iterates over each operation in the list, adding it to the current balance. If the balance falls below zero at any point, it immediately returns `True`. If the script iterates over all operations without the balance falling below zero, it returns `False`.