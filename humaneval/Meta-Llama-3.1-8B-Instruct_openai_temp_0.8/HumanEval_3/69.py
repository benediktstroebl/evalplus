```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function determines if the balance of a bank account falls below zero at any point.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the account balance falls below zero at any point, False otherwise.
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
    
    # If we have iterated over all operations and the balance has never fallen below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([5, 5, 5, 5, 5]))  # False
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the account balance has ever fallen below zero. It iterates over the operations, updating the balance, and returning True as soon as it detects a negative balance. If it finishes iterating without detecting a negative balance, it returns False.