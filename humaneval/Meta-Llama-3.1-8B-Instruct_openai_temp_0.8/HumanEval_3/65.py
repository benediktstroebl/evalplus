```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of deposit and withdrawal operations on a bank account as input.
    It returns True if at any point the balance of account falls below zero, otherwise it returns False.
    
    Parameters:
    operations (List[int]): A list of deposit and withdrawal operations.
    
    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    
    # Initialize the balance to 0
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # If the balance is negative, return True
        if balance < 0:
            return True
    
    # If we've iterated over all operations and the balance is still non-negative, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we define a function `below_zero` that takes a list of operations as input. We initialize the balance to 0 and then iterate over each operation in the list. For each operation, we update the balance by adding the current operation. If the balance falls below 0 at any point, we immediately return True. If we've iterated over all operations and the balance is still non-negative, we return False. The test cases demonstrate the function's behavior with different inputs.