```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.

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
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 2, 3, -10]))  # True
print(below_zero([10, 20, 30]))  # False
```

In this script, we initialize a `balance` variable to 0, which represents the initial balance of the account. We then iterate over each operation in the list, adding it to the balance. If at any point the balance falls below 0, we immediately return `True`. If we finish iterating over all operations without the balance falling below 0, we return `False`.