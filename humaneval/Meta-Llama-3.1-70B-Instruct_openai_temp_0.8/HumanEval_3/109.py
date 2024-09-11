```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

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
print(below_zero([-1, -2, -3]))  # True
print(below_zero([0, 0, 0]))  # False
```

This script defines the `below_zero` function, which initializes a `balance` variable to 0. It then iterates over the `operations` list, adding each operation to the balance. If the balance falls below 0 at any point, the function immediately returns `True`. If the function completes the iteration without the balance falling below 0, it returns `False`. The script includes test cases to demonstrate the function's behavior.