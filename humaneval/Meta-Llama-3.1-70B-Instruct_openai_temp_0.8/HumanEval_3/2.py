```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


# Example usage:
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([-1, 2, 3]))  # True
    print(below_zero([10, -5, 3, -20]))  # True
```

This script defines a function `below_zero` that takes a list of operations, iterates over them, and updates the balance accordingly. If at any point the balance falls below zero, the function returns `True`. Otherwise, it returns `False`. The script includes example usage to demonstrate the function's behavior.