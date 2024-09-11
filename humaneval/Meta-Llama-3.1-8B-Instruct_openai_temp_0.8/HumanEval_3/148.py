```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit (-1 to add a deposit, 1 to add a withdrawal) operations on a bank account.

    Returns:
    bool: True if the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance for each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    return False  # If the loop completes without the balance falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of deposit and withdrawal operations as input. It initializes a balance to zero and updates it for each operation. As soon as the balance falls below zero, it returns True; otherwise, it returns False after all operations have been processed.