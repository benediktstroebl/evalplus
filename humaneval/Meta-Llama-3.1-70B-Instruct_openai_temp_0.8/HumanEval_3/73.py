```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of an account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation amount
        balance += operation
        
        # Check if the balance falls below zero
        if balance < 0:
            # If it does, return True
            return True
    
    # If the function hasn't returned True by now, it means the balance never fell below zero
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([0, 0, 0]))  # False
```