```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if at any point the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to 0
    for op in operations:  # Iterate over each operation
        balance += op  # Update balance by adding the current operation
        if balance < 0:  # Check if balance falls below 0
            return True  # If yes, return True
    return False  # If no, return False after iterating over all operations

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, 3, -2]))  # True
print(below_zero([5, 10, 15]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a balance to 0 and then iterates over each operation, updating the balance and checking if it falls below 0. If it does, the function returns True; otherwise, it returns False after iterating over all operations. The test cases demonstrate the function's behavior with different lists of operations.