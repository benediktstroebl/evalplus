```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: False if the balance never falls below zero, True otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below 0
            return True  # Return True if the balance falls below 0
    return False  # Return False if the balance never falls below 0

# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of bank account operations as input. The function iterates over each operation, adds it to the balance, and checks if the balance falls below zero. If it does, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`. The script also includes example use cases to demonstrate the function's behavior.