```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of the account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


# Test cases
if __name__ == "__main__":
    assert not below_zero([1, 2, 3])
    assert below_zero([1, 2, -4, 5])
    assert not below_zero([])
    assert below_zero([-1])
```
This script defines a function `below_zero` that iterates over the list of operations, maintaining a running balance. If the balance ever falls below zero, the function immediately returns `True`. If the function iterates over all operations without the balance falling below zero, it returns `False`. The script also includes test cases to verify the function's correctness.