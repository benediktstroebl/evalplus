```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    return False  # If the loop completes without the balance falling below zero, return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 2, -3]))  # True
print(below_zero([10, 5, 2, 3]))  # False
```

This script defines a function `below_zero` that takes a list of bank account operations as input. It initializes a `balance` variable to zero and iterates through the list of operations, updating the balance after each operation. If the balance falls below zero at any point, the function immediately returns `True`. If the loop completes without the balance falling below zero, the function returns `False`. The example usage demonstrates the function's behavior with different input scenarios.