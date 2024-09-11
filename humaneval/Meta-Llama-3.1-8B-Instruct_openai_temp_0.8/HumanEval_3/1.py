```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, immediately return True
    return False  # If we've iterated over the entire list without returning True, return False

# Example use cases:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines the `below_zero` function, which takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes the balance to zero, then iterates over each operation in the list, updating the balance and checking if it falls below zero. If it does, the function immediately returns `True`. If the function completes the iteration without finding a balance below zero, it returns `False`.