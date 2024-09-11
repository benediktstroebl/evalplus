```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance ever falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Apply each operation to the balance
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If it has, return True immediately
    return False  # If we've checked all operations without falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance ever falls below zero, and `False` otherwise. It uses a simple iterative approach to simulate the operations on the account and check the balance after each operation. If the balance ever falls below zero, it returns `True` immediately. If it checks all operations without finding a balance below zero, it returns `False`.