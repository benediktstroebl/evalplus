```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Add the operation to the balance
        if balance < 0:  # If the balance is less than 0
            return True  # Return True as the balance falls below 0
    return False  # If the loop completes and the balance is not less than 0, return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and checks if the balance falls below 0 at any point. It initializes the balance to 0 and iterates over each operation in the list, updating the balance and checking if it falls below 0. If it does, the function returns True; otherwise, it returns False after completing the loop. The test cases are included at the end to demonstrate the function's behavior.