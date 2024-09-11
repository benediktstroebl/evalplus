```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

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


# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7, 3]))  # True
print(below_zero([-1, 2, 3, 4]))  # True
print(below_zero([0, 0, 0]))  # False
```