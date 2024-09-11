```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function determines if a bank account balance falls below zero at any point.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation
        balance += operation
        
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is still non-negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the account balance falls below zero at any point, and `False` otherwise. The function initializes the balance to zero and then iterates over each operation in the list, updating the balance and checking if it falls below zero. If the balance falls below zero at any point, the function returns `True` immediately. If we've iterated over all operations and the balance is still non-negative, the function returns `False`. The script includes test cases to demonstrate the function's behavior.