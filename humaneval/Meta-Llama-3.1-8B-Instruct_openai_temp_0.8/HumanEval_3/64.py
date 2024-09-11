```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the loop completes without the balance falling below zero, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 3, -2]))  # True
print(below_zero([5, 2, 8]))  # False
```

This script defines the `below_zero` function, which takes a list of operations (integers representing deposits or withdrawals) and returns a boolean indicating whether the balance falls below zero at any point. The function initializes the balance to 0, then iterates over each operation, updating the balance and checking if it falls below zero. If the balance falls below zero, the function returns `True` immediately; otherwise, it returns `False` after completing the loop. The script also includes test cases to demonstrate the function's behavior.