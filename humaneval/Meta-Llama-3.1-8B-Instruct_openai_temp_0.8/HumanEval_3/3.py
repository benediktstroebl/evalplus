```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.
            Positive numbers represent deposits, negative numbers represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance as 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance by adding the operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, return True immediately
    return False  # If we've iterated over all operations without returning True, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we initialize the balance to 0 and then iterate over each operation in the `operations` list. For each operation, we update the balance by adding the operation. If the balance falls below 0 at any point, we immediately return True. If we've iterated over all operations without returning True, we return False, indicating that the balance never fell below 0.