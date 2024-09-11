```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Subtract the operation from the balance
        balance -= operation
        
        # If the balance falls below 0, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True, the balance never fell below 0
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance ever falls below 0, and `False` otherwise. It uses a simple loop to iterate over the operations, subtracting each one from the balance and checking if it falls below 0. If it does, the function immediately returns `True`. If the loop completes without returning `True`, the function returns `False`. The script also includes test cases to verify the function's behavior.