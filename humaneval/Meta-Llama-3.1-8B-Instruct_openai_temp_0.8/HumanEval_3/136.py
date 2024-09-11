```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point given a list of operations.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation
        balance += operation
        
        # If the balance is below zero, return True
        if balance < 0:
            return True
    
    # If the loop completes without the balance going below zero, return False
    return False

# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -10]))  # False
print(below_zero([-5, -3, -5, 2]))  # True
```