```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate through each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True
    return False  # If the balance never falls below zero, return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function, which takes a list of deposit and withdrawal operations as input. It initializes the account balance to zero and then iterates through each operation, updating the balance accordingly. If at any point the balance falls below zero, the function immediately returns `True`. If the function iterates through all operations without the balance falling below zero, it returns `False`. The script also includes example usage to demonstrate the function's behavior.