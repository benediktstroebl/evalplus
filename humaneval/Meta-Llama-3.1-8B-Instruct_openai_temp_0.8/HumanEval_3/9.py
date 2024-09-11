```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, it means the balance never fell below zero
    return False

# Test the function
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script does the following:

*   Defines a function `below_zero` that takes a list of operations as input.
*   Initializes an `balance` variable to zero.
*   Iterates over each operation in the list, updating the `balance` by adding or subtracting the operation value.
*   Checks if the `balance` falls below zero. If it does, the function returns `True`.
*   If the function hasn't returned `True` by the end of the iteration, it means the `balance` never fell below zero, so the function returns `False`.
*   Tests the function with the provided example inputs.