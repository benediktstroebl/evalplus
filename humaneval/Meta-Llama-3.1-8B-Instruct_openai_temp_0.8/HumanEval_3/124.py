```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:
        # For each operation, update the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True after checking all operations, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance of the account falls below zero at any point, and `False` otherwise. The function iterates over the list of operations, updating the balance after each operation. If the balance falls below zero, it immediately returns `True`. If it checks all operations without returning `True`, it returns `False`.