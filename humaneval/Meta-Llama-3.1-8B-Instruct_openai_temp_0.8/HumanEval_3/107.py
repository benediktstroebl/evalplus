```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Apply each operation to the balance
        if balance < 0:
            return True  # If the balance falls below zero, return True immediately
    return False  # If we've applied all operations without falling below zero, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([0, 0, 0]))  # False
print(below_zero([-1, -2, -3]))  # True
```

This script defines the `below_zero` function which takes a list of operations as input, applies each operation to the balance, and returns True if the balance ever falls below zero. If the balance never falls below zero after applying all operations, the function returns False. The script then includes some test cases to verify the correctness of the function.