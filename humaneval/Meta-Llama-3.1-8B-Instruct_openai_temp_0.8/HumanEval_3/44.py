### Detecting a Bank Account Balance Below Zero
Below is a self-contained Python script that solves the problem of detecting when a bank account balance falls below zero.

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # If the loop completes without returning True, return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
print(below_zero([10, -5, 2, -3]))  # Output: True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list. For each operation, we add it to the balance and check if it falls below zero. If it does, we return True immediately. If the loop completes without returning True, we return False, indicating that the balance never fell below zero.