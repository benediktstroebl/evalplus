```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  
        # For each operation, add it to the balance
        balance += operation  
        # If the balance is negative, return True
        if balance < 0:
            return True
    # If the loop completes without the balance becoming negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes the balance to zero and then updates it by adding each operation. If the balance becomes negative at any point, the function returns `True`. If the loop completes without the balance becoming negative, the function returns `False`. The test cases demonstrate the function's behavior.