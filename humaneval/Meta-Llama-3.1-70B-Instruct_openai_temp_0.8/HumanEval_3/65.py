```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
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
    
    # If the function hasn't returned True by now, it means the balance never fell below zero
    # So, return False
    return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 2, 3, -10]))  # True
```