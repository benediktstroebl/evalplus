```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, the balance never fell below zero, so return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```
This script defines a function `below_zero` that takes a list of integers representing bank account operations and returns a boolean indicating whether the balance ever fell below zero. The function iterates over each operation, adding it to the balance, and returns True as soon as the balance falls below zero. If the balance never falls below zero, the function returns False. The script then includes test cases to demonstrate the function's behavior.