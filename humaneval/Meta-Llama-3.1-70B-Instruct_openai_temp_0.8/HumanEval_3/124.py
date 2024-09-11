```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.
    
    Args:
        operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.
        
    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:
        balance += operation  # Update the balance after each operation
        
        if balance < 0:
            return True  # If balance falls below zero, return True
    
    return False  # If balance never falls below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7, 3]))  # True
print(below_zero([5, 5, 5, 5]))  # False
```

This script defines a function `below_zero` that iterates over the list of operations, updating the balance after each operation. If the balance falls below zero at any point, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.