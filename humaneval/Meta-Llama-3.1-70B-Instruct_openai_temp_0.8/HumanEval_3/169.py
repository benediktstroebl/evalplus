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

# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([0, 0, 0]))  # False
```

This script defines the `below_zero` function, which takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It iterates through each operation, updating the balance and checking if it's below zero. If it is, the function immediately returns `True`. If it finishes iterating through all operations without the balance falling below zero, it returns `False`.