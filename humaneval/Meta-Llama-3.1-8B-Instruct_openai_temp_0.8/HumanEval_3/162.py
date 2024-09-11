```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, immediately return True
    return False  # If the loop completes without the balance falling below zero, return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which takes a list of operations and checks if the balance falls below zero at any point. The function uses a simple iterative approach, updating the balance by adding each operation and checking if it falls below zero. If it does, the function immediately returns True; otherwise, it returns False after completing the loop.