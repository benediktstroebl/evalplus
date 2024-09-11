```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:
        balance += operation  # Update the balance after each operation
        
        # If the balance falls below zero, return True immediately
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, it means the balance never fell below zero
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that iterates over the list of operations, updating the balance after each operation. If the balance ever falls below zero, it immediately returns `True`. If it finishes iterating over all operations without the balance falling below zero, it returns `False`.