```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
    
    Returns:
    bool: True if the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:
        balance += operation  # For each operation, add it to the balance
        if balance < 0:  # If the balance is negative, return True
            return True
    return False  # If the loop completes without the balance being negative, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, 2, 1, 1]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account. It initializes a balance variable to 0 and iterates over the operations, adding each operation to the balance. If the balance becomes negative at any point, the function immediately returns `True`. If the loop completes without the balance being negative, the function returns `False`. The script then demonstrates the function's behavior with several test cases.