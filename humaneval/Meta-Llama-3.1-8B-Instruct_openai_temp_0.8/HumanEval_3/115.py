```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([10, -5, 2, -3]))  # Expected output: True
print(below_zero([10, 5, 2]))  # Expected output: False
```

In this script, we define a function `below_zero` that takes a list of operations as input. We initialize the balance to zero and then iterate over each operation in the list. For each operation, we add it to the balance and check if the balance falls below zero. If it does, we return True immediately. If we finish iterating over all operations without the balance falling below zero, we return False.