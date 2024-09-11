```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below 0
            return True  # If it does, return True
    return False  # If the loop completes without the balance falling below 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -10, 1, -1]))  # False
print(below_zero([-10, 20, -30]))  # True
```

This Python script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. The function initializes the balance to 0 and iterates over each operation, updating the balance and checking if it falls below 0. If it does, the function returns True; otherwise, it returns False. The script includes test cases to demonstrate the function's behavior.