```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    
    # Initialize balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation
        balance += operation
        
        # If the balance is less than 0, return True
        if balance < 0:
            return True
            
    # If the function hasn't returned True after iterating over all operations, return False
    return False

# Test the function
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```
This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It initializes a balance variable to 0, then iterates over each operation in the list, updating the balance and checking if it's less than 0. If the balance is less than 0, it immediately returns `True`. If it iterates over all operations without the balance falling below 0, it returns `False`. The script also includes test cases to verify the function's behavior.