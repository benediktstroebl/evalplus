### Bank Account Balance Checker

Below is a Python script that implements the `below_zero` function to check if a bank account balance falls below zero at any point given a list of operations.

```markdown
### below_zero function
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account balance falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example usage:
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

In this script, the `below_zero` function iterates through each operation in the list, updating the account balance accordingly. If the balance falls below zero, it immediately returns `True`. If the function iterates through all operations without ever returning `True`, it returns `False`, indicating that the balance never fell below zero.