```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    This function checks if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If the loop completes without finding a balance below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of deposit and withdrawal operations and returns `True` if the balance falls below zero at any point and `False` otherwise. The function initializes the balance to zero and then iterates over each operation in the list, updating the balance and checking if it falls below zero. If it does, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.