```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7]))  # True
print(below_zero([-5, 10, -3, 2]))  # True
print(below_zero([5, 10, 20]))  # False
```

This script defines a function `below_zero` that takes a list of operations as input. It initializes a balance variable to 0 and iterates over the operations. For each operation, it adds the operation amount to the balance. If the balance falls below 0 at any point, it immediately returns `True`. If it iterates over all operations without the balance falling below 0, it returns `False`. The script also includes several test cases to demonstrate the function's behavior.