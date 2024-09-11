```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    Detects if at any point the balance of an account falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """

    # Initialize balance to zero
    balance = 0
    
    # Iterate over each operation in the list of operations
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # Check if the balance has fallen below zero
        if balance < 0:
            # If the balance is below zero, return True immediately
            return True
    
    # If the function hasn't returned True after checking all operations, the balance never fell below zero, so return False
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, 1, 1, 1]))  # False
```