```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of the account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # Check if the balance is less than zero
            return True  # Return True if the balance falls below zero
    return False  # If the loop completes without the balance falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

In this script, we first initialize the balance to zero. Then, we iterate over each operation in the list. For each operation, we add it to the balance. If the balance becomes less than zero, we immediately return True. If the loop completes without the balance falling below zero, we return False. This way, we can efficiently detect if the balance of the account falls below zero at any point.