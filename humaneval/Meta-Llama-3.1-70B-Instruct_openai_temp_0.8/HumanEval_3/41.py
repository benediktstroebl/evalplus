```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero after a series of operations.

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

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we initialize the balance to zero and then iterate over each operation. We update the balance by adding the current operation. If the balance falls below zero at any point, we immediately return `True`. If we finish iterating over all operations without the balance falling below zero, we return `False`.