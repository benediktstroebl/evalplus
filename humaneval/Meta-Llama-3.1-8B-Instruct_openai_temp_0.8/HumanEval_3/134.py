```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below 0, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and haven't returned True, the balance never fell below 0
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which takes a list of operations as input and returns a boolean indicating whether the balance ever fell below 0. It initializes the balance to 0 and then iterates over each operation in the list, updating the balance and checking if it falls below 0. If it does, the function immediately returns True. If it completes the iteration without returning True, the balance never fell below 0, so the function returns False. The script also includes test cases to demonstrate the function's behavior.