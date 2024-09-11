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
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance falls below zero
            return True  # Return True as per the problem statement
    return False  # If no operation caused the balance to fall below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines the `below_zero` function which iterates through the list of operations, updating the balance after each operation. If the balance falls below zero at any point, it immediately returns `True`. If no operation causes the balance to fall below zero, it returns `False` at the end. The test cases are included to verify the function's behavior.