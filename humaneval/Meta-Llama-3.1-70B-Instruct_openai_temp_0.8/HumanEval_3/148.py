```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of the account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if at any point the balance of the account falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, -2, -3]))  # True
print(below_zero([10, -5, 5]))  # False
```

This script defines a function `below_zero` that takes a list of operations (deposits and withdrawals) as input. It initializes a balance variable to zero and then iterates over the operations, updating the balance accordingly. If at any point the balance falls below zero, the function immediately returns `True`. If the function completes the iteration without the balance falling below zero, it returns `False`.