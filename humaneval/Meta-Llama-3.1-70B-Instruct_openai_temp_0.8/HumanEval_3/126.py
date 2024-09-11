```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point
    after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit and withdrawal operations.
            Positive values represent deposits and negative values represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """

    # Initialize the balance to zero
    balance = 0

    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation amount
        balance += operation

        # If the balance falls below zero, return True
        if balance < 0:
            return True

    # If the function hasn't returned True after iterating over all operations, 
    # it means the balance never fell below zero, so return False
    return False


# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines the `below_zero` function as specified in the problem, and then provides example usage to demonstrate its functionality. The function iterates over the list of operations, updating the balance after each operation and checking if it falls below zero. If it does, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`.