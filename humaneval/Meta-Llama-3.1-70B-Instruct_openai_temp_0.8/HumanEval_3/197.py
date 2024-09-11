```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance based on the current operation
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True after iterating over all operations, 
    # it means the balance never fell below zero, so return False
    return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, -3]))  # True
print(below_zero([1, 1, 1]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account. It iterates over each operation, updating the balance accordingly, and returns `True` as soon as the balance falls below zero. If the function iterates over all operations without the balance falling below zero, it returns `False`. The script also includes some test cases to demonstrate its usage.