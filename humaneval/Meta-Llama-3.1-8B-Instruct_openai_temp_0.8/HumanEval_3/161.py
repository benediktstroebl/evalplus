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
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation
        
        # If the balance is negative, return True
        if balance < 0:
            return True
    
    # If we've iterated over the entire list and the balance is still non-negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance of the account falls below zero at any point, and `False` otherwise. It initializes the balance to zero and iterates over each operation in the list, updating the balance accordingly. If the balance becomes negative, it immediately returns `True`. If it iterates over the entire list without the balance becoming negative, it returns `False`. The script includes two test cases to demonstrate the function's behavior.