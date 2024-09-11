```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function determines if at any point the balance of a bank account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance by adding the current operation
        
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    
    return False  # If no operation caused the balance to fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input. It initializes the balance to 0 and then iterates over each operation, updating the balance and checking if it falls below 0. If it does, the function returns `True` immediately. If no operation causes the balance to fall below 0, the function returns `False`. The script then includes test cases to demonstrate the function's behavior.