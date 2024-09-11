```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
        bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the current operation to the balance
        if balance < 0:  # Check if the balance has fallen below 0
            return True  # If it has, immediately return True
    return False  # If the loop completes without the balance falling below 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that checks if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations. The function starts with a balance of 0, adds each operation to the balance, and returns True as soon as the balance falls below 0. If the balance never falls below 0, the function returns False. The test cases at the end of the script demonstrate the function's behavior.