```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance with 0
    for operation in operations:
        balance += operation  # Update the balance by adding the operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If the balance is below zero, return True immediately
    return False  # If the function hasn't returned True, it means the balance never fell below zero


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes the balance to 0 and iterates over the operations, updating the balance by adding the operation. If the balance falls below zero, the function returns `True` immediately. If the function hasn't returned `True` by the end of the iteration, it means the balance never fell below zero, so the function returns `False`. The script includes two test cases to demonstrate the function's behavior.