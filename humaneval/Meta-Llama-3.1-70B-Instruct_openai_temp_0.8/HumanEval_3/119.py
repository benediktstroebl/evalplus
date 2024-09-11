```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation amount
        balance += operation
        
        # Check if the balance has fallen below zero
        if balance < 0:
            # If the balance is below zero, return True immediately
            return True
    
    # If the function hasn't returned True after iterating over all operations,
    # it means the balance never fell below zero, so return False
    return False


# Example use cases:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```