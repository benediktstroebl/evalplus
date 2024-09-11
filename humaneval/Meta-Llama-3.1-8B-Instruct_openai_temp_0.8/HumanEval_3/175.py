```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance falls below zero
            return True  # Return True immediately
    return False  # If the loop completes without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script uses a simple for loop to iterate over the operations list. It keeps track of the current balance and checks if it falls below zero after each operation. If it does, the function immediately returns True. If the loop completes without the balance falling below zero, the function returns False.