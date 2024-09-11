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
print(below_zero([0, 0, 0]))  # False
```
This script defines the `below_zero` function, which initializes a balance to 0 and then iterates over the list of operations, adding each operation to the balance. If the balance ever falls below 0, the function immediately returns `True`. If the function iterates over all operations without the balance falling below 0, it returns `False`. The script also includes some test cases to demonstrate the function's behavior.