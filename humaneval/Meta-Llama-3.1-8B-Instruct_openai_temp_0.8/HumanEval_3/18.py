```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
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
    
    # If the loop completes without the balance falling below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. The function initializes the balance to zero and then iterates over each operation in the list, updating the balance and checking if it falls below zero. If it does, the function immediately returns `True`. If the loop completes without the balance falling below zero, the function returns `False`.