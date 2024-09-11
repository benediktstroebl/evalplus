```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance ever falls below zero.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance ever falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    
    for operation in operations:
        balance += operation  # Add the current operation to the balance
        
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    
    return False  # If we've iterated over all operations and the balance is never below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing bank account operations, and returns a boolean indicating whether the balance ever falls below zero. The function iterates over the operations, updating the balance and checking if it falls below zero. If it does, the function returns True immediately. If it iterates over all operations without the balance falling below zero, it returns False. The test cases at the end demonstrate the function's usage.