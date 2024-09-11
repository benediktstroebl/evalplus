```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list of operations
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below 0, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is still non-negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([5, 3, -1, -2]))  # False
print(below_zero([-2, 1, -3, 2]))  # True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account. It initializes the balance to 0 and then iterates over each operation, adding it to the balance. If the balance falls below 0, it immediately returns True. If it iterates over all operations without the balance falling below 0, it returns False. The script also includes test cases to verify the function's behavior.