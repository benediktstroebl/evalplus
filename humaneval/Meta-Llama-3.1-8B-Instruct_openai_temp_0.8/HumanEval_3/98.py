```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:
        balance += operation  # Update the balance after each operation
        
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    
    return False  # Return False if the loop completes without the balance falling below zero


# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([1, 1, 1, 1, 1]))  # False
```

This script defines a function `below_zero` that takes a list of deposit and withdrawal operations as input and returns a boolean indicating whether the balance falls below zero at any point. It uses a simple loop to update the balance after each operation and checks for the condition where the balance falls below zero.