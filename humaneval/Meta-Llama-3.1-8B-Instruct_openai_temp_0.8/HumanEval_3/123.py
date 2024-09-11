```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add or subtract the operation from the balance
        
        if balance < 0:  # Check if the balance is less than zero
            return True  # Return True if the balance falls below zero
    
    return False  # If the loop completes without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account. It initializes a `balance` variable to zero and then iterates over each operation in the list, adding or subtracting it from the balance. If the balance falls below zero at any point, the function immediately returns `True`. If the loop completes without the balance falling below zero, the function returns `False`. The script includes two test cases to demonstrate the function's behavior.