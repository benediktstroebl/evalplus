```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detect if at any point the balance of account falls below zero.

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
print(below_zero([1, 2, 3, 4]))  # False
print(below_zero([-1, -2, -3]))  # True
```

This script provides a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function maintains a running balance by summing each operation to the current balance. If the balance becomes negative, it immediately returns `True`. If all operations are processed without the balance falling below zero, it returns `False`. The script also includes test cases to verify its correctness.