```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # If the balance falls below zero
            return True  # Immediately return True
    return False  # If the loop completes without the balance falling below zero, return False

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-10, -20, -30]))  # True
print(below_zero([100, 200, 300]))  # False
```

This script defines a function `below_zero` that iterates over a list of operations, updating the balance and checking if it falls below zero. If it does, the function immediately returns `True`. Otherwise, it returns `False` after completing the loop. The example usage demonstrates the function's behavior with different inputs.