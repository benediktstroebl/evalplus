```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of deposit and withdrawal operations on a bank account that starts with 
    zero balance. It checks if at any point the balance of account falls below zero and returns True 
    at that point. Otherwise, it returns False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

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
    
    # If the function hasn't returned True by now, it means the balance never fell below 0, so return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance ever falls below zero, and `False` otherwise. The function initializes the balance to 0 and then iterates over each operation in the list, adding it to the balance and checking if the balance has fallen below 0. If it has, the function returns `True`. If the function hasn't returned `True` by the end of the iteration, it means the balance never fell below 0, so it returns `False`.