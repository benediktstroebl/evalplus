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
print(below_zero([-1, -2, -3]))  # True
print(below_zero([5, 5, 5]))  # False
```

In this script, we initialize the `balance` variable to zero. We then iterate over each operation in the list. For each operation, we add it to the balance and check if the balance is less than zero. If it is, we immediately return `True`. If we finish iterating over the list without finding a balance of less than zero, we return `False`.