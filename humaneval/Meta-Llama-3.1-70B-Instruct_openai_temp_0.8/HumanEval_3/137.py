```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7, 2]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([100, 200, 300]))  # False
```
This Python script defines a function `below_zero` that takes a list of deposit and withdrawal operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function initializes a `balance` variable to zero and iterates through each operation in the list. For each operation, it updates the balance and checks if the balance is less than zero. If the balance is less than zero, it immediately returns `True`. If it iterates through all operations without the balance falling below zero, it returns `False`. The script also includes several test cases to demonstrate its usage.