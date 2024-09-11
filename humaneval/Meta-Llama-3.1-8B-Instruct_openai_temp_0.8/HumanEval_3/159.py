```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function determines if the balance of a bank account falls below zero at any point.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance is below 0, return True
        if balance < 0:
            return True
    
    # If the loop completes without the balance falling below 0, return False
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which takes a list of operations as input and returns a boolean indicating whether the balance of the account falls below zero at any point. It uses a single loop to iterate over the operations, updating the balance and checking if it falls below zero. If the balance falls below zero, the function returns True immediately. If the loop completes without the balance falling below zero, the function returns False.