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
    
    # Initialize balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance is negative, return True
        if balance < 0:
            return True
    
    # If we've iterated over the entire list and the balance is still non-negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. It initializes a `balance` variable to 0 and iterates over each operation in the list, adding it to the balance. If the balance becomes negative at any point, it immediately returns `True`. If it iterates over the entire list without the balance becoming negative, it returns `False`. The test cases demonstrate the function's behavior with different inputs.