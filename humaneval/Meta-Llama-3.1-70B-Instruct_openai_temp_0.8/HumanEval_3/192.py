```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero 
    after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations. 
                             Positive integers represent deposits and 
                             negative integers represent withdrawals.

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
print(below_zero([10, -20, 30, -40]))  # True
print(below_zero([-10, 20, -30, 40]))  # True
print(below_zero([10, 20, 30, 40]))  # False
```