```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate through each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # If the balance is below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True after iterating through all operations, 
    # it means the balance never fell below zero, so return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([1, 1, 1]))  # Expected output: False
print(below_zero([-1, -1, -1]))  # Expected output: True
```