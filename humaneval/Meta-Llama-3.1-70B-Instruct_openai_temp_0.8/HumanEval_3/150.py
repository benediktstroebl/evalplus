```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

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
print(below_zero([1, -2, 3, -4, 5]))  # True
print(below_zero([1, 2, 3, 4, 5]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a variable `balance` to zero, then iterates over the operations, updating the balance after each operation. If the balance falls below zero, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.