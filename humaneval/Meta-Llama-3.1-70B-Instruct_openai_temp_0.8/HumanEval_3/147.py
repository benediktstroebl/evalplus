```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

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

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([1, -2, -3]))  # True
```

This script defines the `below_zero` function as specified. It initializes a variable `balance` to zero and iterates over the list of operations, adding each operation to the balance. If the balance ever falls below zero, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`. The test cases at the end demonstrate the function's behavior with different inputs.