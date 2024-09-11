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
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines the `below_zero` function as specified. It initializes a `balance` variable to 0 and then iterates over the `operations` list. For each operation, it updates the `balance` by adding the operation amount. If the `balance` ever falls below 0, the function immediately returns `True`. If the function iterates over all operations without the `balance` falling below 0, it returns `False`.