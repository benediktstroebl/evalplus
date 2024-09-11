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
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance is below zero, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is not below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script first initializes the balance to zero. It then iterates over each operation in the list, adding each operation to the balance. If the balance ever falls below zero, it immediately returns `True`. If it iterates over all operations without the balance falling below zero, it returns `False`.