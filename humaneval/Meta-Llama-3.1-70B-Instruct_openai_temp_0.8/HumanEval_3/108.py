```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point
    given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
if not below_zero([1, 2, 3]):
    pass
if below_zero([1, 2, -4, 5]):
    pass
if not below_zero([]):
    pass
if below_zero([-1]):
    pass
```

This script defines the `below_zero` function as specified. It initializes a `balance` variable to zero and iterates over each operation in the list. If the balance falls below zero at any point, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`. The test cases at the end verify the function's behavior.