```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account's balance falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:
        balance += operation  # Update balance after each operation
        if balance < 0:  # Check if balance falls below zero
            return True
    return False  # If no operations caused balance to fall below zero, return False


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # Expected output: False
    print(below_zero([1, 2, -4, 5]))  # Expected output: True
    print(below_zero([10, -5, -3, -2]))  # Expected output: True
    print(below_zero([10, 5, 3, 2]))  # Expected output: False
```

This script defines the `below_zero` function as specified, which iterates over each operation in the input list, updating the balance accordingly. If the balance falls below zero at any point, the function immediately returns `True`. If the function completes the iteration without finding a negative balance, it returns `False`. The script also includes test cases to demonstrate its usage.