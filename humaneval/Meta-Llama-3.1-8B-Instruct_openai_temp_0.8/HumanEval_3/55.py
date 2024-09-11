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
        # Update the balance by adding or subtracting the operation value
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the loop completes without the balance falling below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It initializes the balance to zero and then iterates over each operation, updating the balance and checking if it falls below zero. If it does, the function returns True; otherwise, it returns False. The test cases at the end demonstrate the function's behavior.