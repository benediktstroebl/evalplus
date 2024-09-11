```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

In this script, we initialize a variable `balance` to 0, representing the initial balance of the account. We then iterate through each operation in the list, adding it to the balance. If the balance ever falls below 0, we immediately return `True`. If we finish iterating through all operations without the balance falling below 0, we return `False`.