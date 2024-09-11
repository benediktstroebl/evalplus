```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance is negative
            return True  # If the balance is negative, return True
    return False  # If the loop completes without a negative balance, return False


# Test cases
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```

In this script, the `below_zero` function iterates over each operation in the list. It updates the balance by adding the current operation to it. As soon as the balance becomes negative, it immediately returns `True`, indicating that the balance fell below zero at some point. If the function completes the loop without finding a negative balance, it returns `False`, indicating that the balance never fell below zero.

The script also includes two test cases at the end to verify that the function behaves correctly.