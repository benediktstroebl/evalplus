```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize balance to zero
    balance = 0
    
    # Iterate over each operation
    for operation in operations:
        # Update the balance
        balance += operation
        
        # Check if the balance is below zero
        if balance < 0:
            # If balance is below zero, return True
            return True
    
    # If no negative balance is found, return False
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list. For each operation, we update the balance and check if it's below zero. If we find a negative balance, we immediately return `True`. If we finish checking all operations without finding a negative balance, we return `False`.