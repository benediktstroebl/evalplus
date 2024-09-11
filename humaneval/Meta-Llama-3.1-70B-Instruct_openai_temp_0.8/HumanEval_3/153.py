```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    This function checks if the balance of a bank account falls below zero after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance never fell below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we define a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. We initialize a variable `balance` to zero and then iterate over each operation in the list, updating the balance accordingly. If the balance falls below zero at any point, we return `True`. If we've iterated over all operations and the balance never fell below zero, we return `False`.