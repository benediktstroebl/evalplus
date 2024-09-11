### Solution
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations.
        
    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation
    for operation in operations:
        # Update the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the loop completes without balance falling below zero, return False
    return False

# Test the function
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input. It keeps track of the current balance by iterating over each operation, adding it to the balance, and checking if the balance falls below zero. If it does, the function immediately returns `True`. If the function completes the loop without the balance falling below zero, it returns `False`. The script also includes test cases to verify the function's correctness.