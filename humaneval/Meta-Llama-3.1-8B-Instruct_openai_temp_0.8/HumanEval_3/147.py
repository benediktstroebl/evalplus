### Bank Account Balance Checker
Below is a self-contained Python script that solves the problem. This script defines a function `below_zero` that checks if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account that starts with zero balance.

    Returns:
    bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance by adding the operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance does not fall below zero

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether the balance falls below zero at any point. The function initializes the balance to zero and then iterates over each operation, updating the balance and checking if it falls below zero. If it does, the function returns True; otherwise, it returns False. The script also includes example usage demonstrating the function's behavior with different inputs.