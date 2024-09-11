```markdown
### Self-contained Python script to detect if account balance falls below zero

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the account balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to 0
    for operation in operations:
        balance += operation  # Update the balance after each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    return False  # Return False if the balance never falls below zero


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations on a bank account as input. It iterates over the operations, updating the balance after each operation. If the balance falls below zero at any point, it returns `True`. Otherwise, it returns `False` if the balance never falls below zero. The script includes test cases to demonstrate the function's behavior.