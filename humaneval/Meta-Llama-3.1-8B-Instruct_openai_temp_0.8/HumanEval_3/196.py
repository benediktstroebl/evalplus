```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize balance to 0
    balance = 0
    
    # Iterate over each operation
    for operation in operations:
        # Add operation to balance
        balance += operation
        
        # If balance is below 0, return True
        if balance < 0:
            return True
    
    # If no operation caused balance to fall below 0, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes the balance to 0 and then iterates over each operation, updating the balance and checking if it falls below 0. If it does, the function returns `True`. If it doesn't after checking all operations, the function returns `False`. The script includes two test cases to demonstrate the function's behavior.