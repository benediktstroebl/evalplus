```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of an account falls below zero.

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
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 2, 3, -10]))  # True
print(below_zero([10, 5, 3, 2]))  # False
```

This Python script defines a function `below_zero` that takes a list of operations as input, where each operation is either a deposit (positive integer) or a withdrawal (negative integer). It iterates over the operations, updating the balance after each operation. If at any point the balance falls below zero, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.