```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation
    for operation in operations:
        # Update the balance
        balance += operation
        
        # Check if the balance is below zero
        if balance < 0:
            # If it is, return True
            return True
    
    # If we've iterated over all operations and the balance hasn't fallen below zero, return False
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```