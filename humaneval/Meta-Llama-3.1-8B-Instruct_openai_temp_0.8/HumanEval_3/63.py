```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero
    after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations

    Returns:
        bool: True if balance falls below zero at any point, False otherwise
    """

    # Initialize the balance to zero
    balance = 0

    # Iterate over each operation in the list
    for operation in operations:
        # Add the operation to the balance
        balance += operation

        # If the balance falls below zero, return True
        if balance < 0:
            return True

    # If the loop completes without returning True, return False
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Should print: False
print(below_zero([1, 2, -4, 5]))  # Should print: True
```

This script defines the `below_zero` function, which checks if the balance of a bank account falls below zero after a series of deposit and withdrawal operations. The function iterates over each operation, updating the balance accordingly. If the balance falls below zero at any point, the function returns `True`. Otherwise, it returns `False` after checking all operations. The script also includes test cases to verify the function's behavior.