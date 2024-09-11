```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
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
print(below_zero([10, -2, 3, -2]))  # False
print(below_zero([-1, -2, -3]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input, simulates the operations on an initial balance of zero, and returns `True` as soon as the balance falls below zero. If the balance remains non-negative after all operations, it returns `False`. The test cases demonstrate the function's behavior in different scenarios.