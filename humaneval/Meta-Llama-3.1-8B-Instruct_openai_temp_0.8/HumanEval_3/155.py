```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of an account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance of account falls below zero at any point, False otherwise.
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
    
    # If the function hasn't returned True after iterating over all operations, the balance never fell below 0
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It does this by initializing the balance to zero and then iterating over each operation, adding it to the balance and checking if the balance falls below zero. If it does, it immediately returns `True`. If it doesn't after iterating over all operations, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.