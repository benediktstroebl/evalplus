```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If the loop completes without the balance falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script uses a simple loop to iterate over the list of operations. For each operation, it adds the operation to the balance. If the balance ever falls below zero, it immediately returns True. If the loop completes without the balance falling below zero, it returns False.