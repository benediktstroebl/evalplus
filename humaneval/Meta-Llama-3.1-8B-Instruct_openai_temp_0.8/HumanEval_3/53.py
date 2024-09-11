```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Subtract the operation from the balance (withdrawal) or add it (deposit)
        balance += operation
        
        # If the balance becomes negative, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is still non-negative, return False
    return False


# Test cases
print(below_zero([1, 2, 3]))     # False
print(below_zero([1, 2, -4, 5])) # True
```