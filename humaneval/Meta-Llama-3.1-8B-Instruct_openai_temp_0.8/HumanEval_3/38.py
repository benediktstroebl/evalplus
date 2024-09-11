```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account. 
                                Deposit is represented by a positive number, and withdrawal is represented by a negative number.

    Returns:
        bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the account balance to zero

    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance

        # Check if the balance falls below zero
        if balance < 0:
            return True  # Return True if the balance falls below zero

    return False  # Return False if the balance never falls below zero


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of deposit and withdrawal operations as input. It initializes the account balance to zero and then iterates over each operation, updating the balance accordingly. If the balance falls below zero at any point, the function returns `True`. If the balance never falls below zero, the function returns `False`. The script includes test cases to demonstrate the function's behavior.