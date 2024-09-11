```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, 
    and at that point function should return True. Otherwise it should return False.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Subtract the operation from the balance (if withdrawal) or add it to the balance (if deposit)
        balance += operation
        
        # If the balance falls below 0, return True
        if balance < 0:
            return True
    
    # If the function hasn't returned True, it means the balance never fell below 0, so return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script uses a variable `balance` to keep track of the current balance in the account. It then iterates over each operation in the list, updating the balance accordingly. As soon as it finds an operation that would cause the balance to fall below 0, it immediately returns `True`. If it gets through the entire list without finding such an operation, it returns `False`.