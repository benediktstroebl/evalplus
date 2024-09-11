```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add or subtract the operation from the balance
        if balance < 0:  # If the balance falls below zero
            return True  # Return True immediately
    return False  # If the loop completes without the balance falling below zero, return False

# Test the function
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we define a function `below_zero` that takes a list of operations as input. We initialize the balance to zero and then iterate over each operation. For each operation, we add or subtract the operation from the balance and check if the balance falls below zero. If it does, we immediately return `True`. If we complete the loop without the balance falling below zero, we return `False`.