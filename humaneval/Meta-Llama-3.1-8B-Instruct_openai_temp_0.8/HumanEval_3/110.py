```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations.
        
    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Subtract the operation from the balance
        balance -= operation
        
        # If the balance is negative, return True immediately
        if balance < 0:
            return True
    
    # If we've iterated over the entire list without returning True, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which iterates over a list of operations and checks if the balance falls below zero. If it does, the function returns `True` immediately. If it doesn't, the function returns `False` after iterating over the entire list. The script also includes test cases to demonstrate the function's behavior.