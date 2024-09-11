```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the loop completes without the balance falling below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that checks if the balance of a bank account falls below zero after a series of deposit and withdrawal operations. It iterates over the operations, updating the balance and checking if it falls below zero. If it does, the function returns `True`. If the loop completes without the balance falling below zero, the function returns `False`. The script also includes example usage to demonstrate the function's behavior.