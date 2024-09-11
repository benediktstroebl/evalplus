```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, 
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance with the current operation
        
        if balance < 0:  # Check if the balance is below zero
            return True  # If the balance is below zero, return True
    
    return False  # If the loop completes without the balance going below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The script also includes test cases to demonstrate the function's behavior.