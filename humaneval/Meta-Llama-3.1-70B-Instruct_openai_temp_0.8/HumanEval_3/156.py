```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list of operations
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # Check if the balance is below zero
        if balance < 0:
            # If the balance is below zero, return True
            return True
    
    # If the function hasn't returned True after iterating over all operations, 
    # it means the balance never fell below zero, so return False
    return False

# Test the function
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It uses a simple iterative approach to keep track of the balance and checks if it falls below zero after each operation.