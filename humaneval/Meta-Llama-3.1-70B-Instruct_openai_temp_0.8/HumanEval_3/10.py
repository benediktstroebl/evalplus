```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

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
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, -3, -2]))  # True
print(below_zero([10, 5, 3, 2]))  # False
```

This script defines a function `below_zero` that iterates over the list of operations, updating the balance accordingly. If the balance falls below zero at any point, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`. The script also includes several test cases to demonstrate the function's behavior.