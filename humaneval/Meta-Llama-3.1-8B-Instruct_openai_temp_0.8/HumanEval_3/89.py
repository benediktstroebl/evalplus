```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance falls below 0
            return True  # Return True immediately
    return False  # If the loop completes without balance falling below 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which iterates over the operations list, tracking the balance. As soon as the balance falls below zero, it returns True. If the loop completes without the balance falling below zero, it returns False. The test cases at the end demonstrate the function's behavior.