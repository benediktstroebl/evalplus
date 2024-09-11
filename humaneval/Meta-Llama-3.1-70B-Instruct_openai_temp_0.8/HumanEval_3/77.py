```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7, 2]))  # True
print(below_zero([5, 5, 5, 5]))  # False
```

This script defines a function `below_zero` that takes a list of operations as input, iterates over each operation, and updates the balance accordingly. As soon as the balance falls below zero, the function returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.