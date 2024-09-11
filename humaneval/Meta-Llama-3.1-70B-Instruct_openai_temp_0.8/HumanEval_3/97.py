```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True
    return False  # If the balance never falls below zero, return False


# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It iterates over each operation, updates the balance, and checks if the balance is below zero after each operation. If the balance falls below zero, it immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`.