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
    balance = 0  # Initialize balance to 0
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update balance by adding the operation
        if balance < 0:  # Check if balance falls below 0
            return True  # Return True if balance falls below 0
    return False  # Return False if balance remains non-negative

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
print(below_zero([1, 2, 3, 4]))  # Expected output: False
```