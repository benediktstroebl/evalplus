```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    balance = 0  # Initialize the balance as zero
    
    # Iterate over each operation in the list
    for operation in operations:
        balance += operation  # Update the balance based on the current operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True after checking all operations, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([-1, 2, 3, 4]))  # True
print(below_zero([1, 2, 3, 4]))  # False
```