```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if it does
    return False  # Return False if the balance never falls below zero


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

In this script, the `below_zero` function iterates over each operation in the list. It updates the balance for each operation and checks if the balance falls below zero. If it does, the function returns True immediately. If it finishes iterating over all operations without returning True, it returns False. The test cases are included at the end of the script to verify the function's correctness.