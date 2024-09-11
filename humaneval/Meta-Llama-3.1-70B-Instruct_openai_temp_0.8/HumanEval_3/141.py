```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point
    after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation amount
        balance += operation
        
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance never fell below zero, return False
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
```
This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It iterates over the operations, updating the balance and checking if it falls below zero at any point. If it does, the function returns `True`; otherwise, it returns `False`. The script includes example usage to demonstrate the function's behavior.