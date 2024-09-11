```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
if below_zero([1, 2, 3]):
    assert False, f"Expected False, got {below_zero([1, 2, 3])}"
if below_zero([1, 2, -4, 5]):
    assert True, f"Expected True, got {below_zero([1, 2, -4, 5])}"
if not below_zero([5, 10, 20]):
    assert True, f"Expected True, got {below_zero([5, 10, 20])}"
if below_zero([-1]):
    assert True, f"Expected True, got {below_zero([-1])}"
```