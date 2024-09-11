```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, 
    and at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below 0
            return True  # Return True if the balance falls below 0
    return False  # Return False if the balance never falls below 0


# Test cases
print(below_zero([1, 2, 3]))  # Should return False
print(below_zero([1, 2, -4, 5]))  # Should return True
print(below_zero([10, -20, 30]))  # Should return False
print(below_zero([-10, 20, -30]))  # Should return True
```

This Python script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a balance to 0 and iterates over the operations, updating the balance after each operation. If the balance ever falls below 0, it immediately returns True. If it finishes iterating over all operations without the balance falling below 0, it returns False. The script includes test cases to demonstrate the function's behavior.