```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if at any point the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance falls below zero, return True
            return True
    return False  # If the loop completes without returning True, return False

# Test the function
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```