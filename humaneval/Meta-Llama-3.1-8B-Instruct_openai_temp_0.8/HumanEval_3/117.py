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
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add or subtract the operation amount from the balance
        if balance < 0:  # Check if the balance falls below 0
            return True  # Return True as soon as the balance falls below 0
    return False  # If the loop completes without the balance falling below 0, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, the `below_zero` function iterates over each operation in the list and updates the balance accordingly. As soon as the balance falls below 0, it returns True. If the loop completes without the balance falling below 0, it returns False. The example usage demonstrates the function's behavior with the provided test cases.