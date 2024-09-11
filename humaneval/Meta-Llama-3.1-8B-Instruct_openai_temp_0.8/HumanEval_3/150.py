```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    return False  # If we've iterated over all operations and the balance hasn't fallen below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list. For each operation, we add it to the balance and check if it's below zero. If it is, we immediately return True. If we've iterated over all operations and the balance hasn't fallen below zero, we return False.