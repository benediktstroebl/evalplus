```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations.
        
    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, return True immediately
    
    return False  # If we've iterated over the entire list without returning True, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, 1, 1, 1, 1]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It keeps track of the running balance and returns `True` as soon as the balance falls below zero, and `False` otherwise. The test cases demonstrate the function's behavior for different input lists.