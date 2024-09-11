```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:
        balance += operation  # Update the balance by adding the operation
        if balance < 0:  # Check if the balance has fallen below 0
            return True  # If it has, return True immediately
    return False  # If the loop completes without the balance falling below 0, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input. It initializes the balance to 0 and then iterates over the operations, updating the balance by adding each operation. If the balance falls below 0 at any point, the function returns True immediately. If the loop completes without the balance falling below 0, the function returns False.