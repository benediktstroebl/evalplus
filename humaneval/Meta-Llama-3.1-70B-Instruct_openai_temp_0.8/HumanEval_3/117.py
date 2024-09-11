```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point after a series of operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations. Positive numbers represent deposits, and negative numbers represent withdrawals.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
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
```

This script works by maintaining a running balance of the account. It iterates over each operation in the list, adding the operation to the balance. If the balance falls below zero at any point, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.