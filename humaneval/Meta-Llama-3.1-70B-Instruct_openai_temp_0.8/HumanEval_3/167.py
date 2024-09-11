```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit (positive integers) and withdrawal (negative integers) operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([10, -5, 2, -7, 1]))  # True
```

This script defines a function `below_zero` that iterates over a list of operations, updating the balance after each operation. If the balance falls below zero, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`. The script includes example use cases to demonstrate the function's behavior.