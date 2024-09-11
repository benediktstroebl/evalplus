```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero, False otherwise.
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
print(below_zero([10, -5, 5]))  # False
```
This script defines a function `below_zero` that iterates over a list of deposit and withdrawal operations, updating the balance after each operation. If at any point the balance falls below zero, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`. The script also includes some test cases to demonstrate the function's behavior.