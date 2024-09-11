```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function detects if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Subtract the operation from the balance
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True
    
    # If we finish iterating over the list without the balance falling below zero, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list. We subtract the operation from the balance, and if the balance falls below zero, we immediately return `True`. If we finish iterating over the list without the balance falling below zero, we return `False`.