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
print(below_zero([10, -5, -7, 2]))  # True
print(below_zero([10, -5, 7, 2]))  # False
```

This script defines a function `below_zero` that iterates through the list of operations, updating the balance at each step. If the balance falls below zero, the function immediately returns `True`. If the function iterates through all operations without the balance falling below zero, it returns `False`. The test cases at the end demonstrate the function's behavior with different inputs.