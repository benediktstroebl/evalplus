```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function determines if at any point the balance of an account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
    
    Returns:
    bool: True if at any point the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding or subtracting the current operation
        balance += operation
        
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    
    # If the loop completes without finding a balance below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that iterates over a list of operations, updating the balance accordingly. If the balance ever falls below zero, it immediately returns `True`. If the loop completes without finding a balance below zero, it returns `False`. The test cases at the end demonstrate the function's behavior for different inputs.