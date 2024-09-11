```markdown
### below_zero Function

#### Problem Statement:

You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance.
The task is to detect if at any point the balance of account falls below zero, and at that point function should return True.
Otherwise, it should return False.

#### Solution:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:
        balance += operation  # Update balance after each operation
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True as soon as balance falls below zero
    return False  # Return False if balance never falls below zero

# Example use cases:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

#### Explanation:

This script defines a function `below_zero` that takes a list of operations as input. It initializes the balance to zero and iterates over each operation in the list. After each operation, it checks if the balance has fallen below zero. If it has, the function immediately returns `True`. If it iterates over all operations without finding a balance below zero, it returns `False`.