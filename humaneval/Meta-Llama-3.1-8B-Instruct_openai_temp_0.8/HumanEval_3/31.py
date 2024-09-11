```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # If the balance is ever negative, return True
        if balance < 0:
            return True
    
    # If we've iterated over the entire list and the balance is never negative, return False
    return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance of the account falls below zero at any point, and `False` otherwise. It uses a simple iterative approach to keep track of the balance and update it based on each operation. If the balance ever goes below zero, it immediately returns `True`. If it iterates over the entire list without finding a negative balance, it returns `False`.