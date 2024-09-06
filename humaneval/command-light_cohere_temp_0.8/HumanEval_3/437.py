```Python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point function should return True. Otherwise, it should return False.
    """
    logic is a simple one, that checks if any operation is less than zero and returns the result."""
bool = any(operations) <= 0
    return bool
```