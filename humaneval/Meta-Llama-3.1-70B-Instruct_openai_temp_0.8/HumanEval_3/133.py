```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if the balance of a bank account falls below zero at any point.

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


# Example use cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([10, -5, -7]))  # True
    print(below_zero([-1, 5, 3]))  # True
    print(below_zero([0, 0, 0]))  # False
```

This script defines a function `below_zero` that takes a list of operations (deposits and withdrawals) and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over the operations, updating the balance after each operation. If the balance becomes negative, the function immediately returns `True`. If the function finishes iterating over all operations without the balance falling below zero, it returns `False`.