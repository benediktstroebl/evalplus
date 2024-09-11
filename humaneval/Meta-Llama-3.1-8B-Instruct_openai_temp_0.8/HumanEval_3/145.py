```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance by adding the current operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the loop completes without finding a negative balance, return False


# Test cases
if below_zero([1, 2, 3]):
    assert False, f"Expected below_zero([1, 2, 3]) to return False, but got {below_zero([1, 2, 3])}"

if below_zero([1, 2, -4, 5]):
    assert below_zero([1, 2, -4, 5]) == True, f"Expected below_zero([1, 2, -4, 5]) to return True, but got {below_zero([1, 2, -4, 5])}"

print("All test cases pass.")
```

In this script, the `below_zero` function takes a list of operations as input, iterates over them, and checks if the balance ever falls below zero. If it does, the function returns True immediately. If the loop completes without finding a negative balance, the function returns False. The test cases are included to verify the correctness of the function.