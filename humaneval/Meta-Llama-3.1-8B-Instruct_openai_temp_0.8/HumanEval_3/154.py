```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ Detect if at any point the balance of account falls below zero.

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
print(below_zero([-5, -3, -2]))  # False
print(below_zero([-5, -3, -2, 1]))  # True
print(below_zero([1, 2, 3, 4, 5]))  # False
```
This Python script defines a function `below_zero` that simulates bank account operations. It iterates over each operation in the list, adding it to the current balance. If the balance falls below zero at any point, the function immediately returns `True`. If the function completes the iteration without finding a balance below zero, it returns `False`. The script includes several test cases to demonstrate its functionality.