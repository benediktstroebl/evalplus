```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the loop completes without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, 1, 1, 1]))  # False
print(below_zero([-1, -1, -1, -1]))  # True
```

In this script, we initialize the balance to zero and then iterate over each operation. For each operation, we add it to the balance. If the balance ever falls below zero, we immediately return True. If the loop completes without the balance falling below zero, we return False.