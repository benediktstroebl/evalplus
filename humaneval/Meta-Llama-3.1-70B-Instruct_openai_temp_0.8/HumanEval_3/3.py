```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account's balance falls below zero 
    after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit and withdrawal operations.
                             Positive values represent deposits, negative values represent withdrawals.

    Returns:
    bool: True if the account balance falls below zero at any point, False otherwise.
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
print(below_zero([-1, 2, 3]))  # True
print(below_zero([10, -5, 5, -15]))  # True
print(below_zero([10, 5, 5, 15]))  # False
```

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes a variable `balance` to zero and then iterates over each operation in the list. For each operation, it updates the balance by adding the operation value. If the balance falls below zero at any point, it immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`. The script also includes several example use cases to demonstrate the function's behavior.