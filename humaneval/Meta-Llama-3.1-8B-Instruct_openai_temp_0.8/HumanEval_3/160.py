```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function takes a list of deposit and withdrawal operations on a bank account that starts with zero balance.
    It returns True if at any point the balance of account falls below zero, otherwise it returns False.

    Args:
        operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize account balance to zero

    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately

    return False  # If the loop completes without the balance falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function as specified. It initializes the account balance to zero and then iterates over each operation in the list. For each operation, it adds the operation to the balance and checks if the balance falls below zero. If it does, it returns `True` immediately. If the loop completes without the balance falling below zero, it returns `False`. The script also includes example usage to demonstrate the function's behavior.