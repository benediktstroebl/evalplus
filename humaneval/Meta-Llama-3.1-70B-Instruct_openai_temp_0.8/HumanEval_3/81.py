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
        # Update the balance by adding the operation
        balance += operation
        
        # If the balance is below zero, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is never below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([10, 20, 30]))  # False
```