```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function detects if at any point the balance of an account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True after iterating over all operations, return False
    return False

# Test cases
print(below_zero([1, 2, 3])) # False
print(below_zero([1, 2, -4, 5])) # True
print(below_zero([10, -5, 5, -5])) # True
print(below_zero([10, 20, 30])) # False
```

This script defines a function `below_zero` that takes a list of integers representing bank account operations and returns a boolean indicating whether the balance ever falls below zero. It uses a simple iterative approach to keep track of the balance and returns as soon as it falls below zero, or False if it never does.