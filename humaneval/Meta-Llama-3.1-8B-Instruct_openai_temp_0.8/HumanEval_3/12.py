```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of the bank account falls below zero.

    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add or subtract the operation from the balance
        if balance < 0:  # If the balance falls below zero
            return True  # Return True immediately
    return False  # If the loop completes without the balance falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list. For each operation, we add it to the balance. If the balance falls below zero at any point, we return True immediately. If the loop completes without the balance falling below zero, we return False.