```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account balance goes below zero 
    given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers where positive values 
            represent deposits and negative values represent withdrawals.

    Returns:
        bool: True if the balance goes below zero at any point, False otherwise.
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
print(below_zero([10, -5, 3, -8]))  # True
print(below_zero([10, 5, 3, 8]))  # False
```