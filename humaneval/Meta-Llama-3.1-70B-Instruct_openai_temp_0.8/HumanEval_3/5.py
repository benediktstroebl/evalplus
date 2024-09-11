```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive int) and withdrawal (negative int) operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, -3, -4, -5]))  # True
print(below_zero([10, -5, 5, -3, 3]))  # False
```

This Python function works by initializing a balance variable to 0 and then iterating through the list of operations. For each operation, it updates the balance by adding the operation amount. If the balance becomes negative at any point, the function immediately returns True. If the function iterates through all operations without the balance falling below 0, it returns False.