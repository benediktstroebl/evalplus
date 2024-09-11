```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Perform the operation
        if balance < 0:  # Check if the balance is below zero
            return True  # If so, return True
    return False  # If no negative balance is found, return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7]))  # True
print(below_zero([5, 5, 5]))  # False
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over the operations, updates the balance, and checks if the balance is below zero after each operation. If a negative balance is found, the function returns `True`. If no negative balance is found after all operations, the function returns `False`. The script also includes some test cases to demonstrate the function's behavior.