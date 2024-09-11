```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
            Positive numbers represent deposits and negative numbers represent withdrawals.

    Returns:
        bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the account balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance never falls below zero

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This Python script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the account balance ever falls below zero. The function uses a simple iterative approach to update the balance and check for negative values. If the balance falls below zero, the function immediately returns `True`. Otherwise, it returns `False` at the end of the iteration. The script also includes test cases to demonstrate the function's behavior.