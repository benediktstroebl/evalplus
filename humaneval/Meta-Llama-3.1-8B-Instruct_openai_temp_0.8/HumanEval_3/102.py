```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point in a list of bank account operations, 
    the balance of the account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance is below zero, return True
        if balance < 0:
            return True
    
    # If the loop completes without the balance falling below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that iterates over a list of operations, updating a running balance. If the balance ever falls below zero, the function immediately returns `True`. If the loop completes without the balance falling below zero, the function returns `False`. The script also includes two test cases to demonstrate the function's behavior.