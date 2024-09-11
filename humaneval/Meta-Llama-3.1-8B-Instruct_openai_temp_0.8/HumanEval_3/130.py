```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance falls below 0, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True by now, it means the balance never fell below 0
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```