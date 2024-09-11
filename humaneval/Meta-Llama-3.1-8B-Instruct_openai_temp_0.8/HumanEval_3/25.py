```markdown
### Solution to the Problem
#### Below Zero Function
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance.
    Your task is to detect if at any point the balance of account falls below zero, and at that point function should return True.
    Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Add the current operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True immediately
    return False  # If the function hasn't returned True by now, it means the balance never fell below zero
```

### Example Usage
```python
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```
This script defines a function `below_zero` that takes a list of operations on a bank account as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over each operation, adding it to the balance, and checks if the balance falls below zero. If it does, the function returns `True` immediately. Otherwise, it returns `False` after iterating over all operations.