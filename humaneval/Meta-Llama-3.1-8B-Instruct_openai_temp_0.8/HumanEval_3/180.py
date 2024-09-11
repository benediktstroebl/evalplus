```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on the bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        
        if balance < 0:  # Check if the balance is less than 0
            return True  # Return True if the balance falls below 0
    
    return False  # If the loop completes without returning, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes the balance to 0 and then iterates over each operation in the list, adding it to the balance. If the balance falls below 0, it immediately returns `True`. If the loop completes without returning, it returns `False`.