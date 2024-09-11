```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if a bank account balance falls below zero after a series of operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.
            Positive numbers represent deposits and negative numbers represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

    balance = 0  # Initialize the account balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If so, return True immediately
    return False  # If the function hasn't returned True after all operations, the balance never fell below zero


# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```
This script defines a function `below_zero` that takes a list of integers representing bank account operations as input. It initializes a balance variable to zero and iterates over each operation in the list, updating the balance accordingly. If the balance falls below zero at any point, the function returns `True`. If the function completes the iteration without returning `True`, it returns `False`, indicating that the balance never fell below zero.