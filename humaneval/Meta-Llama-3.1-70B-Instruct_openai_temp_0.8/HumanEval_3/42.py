```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """

    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Apply the operation to the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations without the balance falling below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7]))  # True
print(below_zero([-1, 5, 3]))  # True
print(below_zero([5, 3, -2, -4, 1]))  # False
```