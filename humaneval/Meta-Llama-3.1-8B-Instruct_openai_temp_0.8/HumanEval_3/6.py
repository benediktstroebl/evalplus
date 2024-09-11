```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, the balance never fell below zero
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of deposit and withdrawal operations as input. It initializes a `balance` variable to zero and then iterates over each operation in the list, adding it to the balance. If the balance falls below zero, the function immediately returns `True`. If the function completes the iteration without returning `True`, it returns `False`, indicating that the balance never fell below zero. The script includes test cases to verify the function's correctness.