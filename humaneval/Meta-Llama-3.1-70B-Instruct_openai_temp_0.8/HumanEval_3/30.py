```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: Whether the balance falls below zero at any point.
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
    print(below_zero([-1, -2, -3]))  # True
    print(below_zero([0, 0, 0]))  # False
```

This Python script defines a function called `below_zero` which takes a list of integers representing deposit and withdrawal operations. It initializes a variable `balance` to zero, then iterates over the list of operations, adding each operation to the balance. If the balance ever falls below zero, the function immediately returns `True`. If it iterates over the entire list without the balance falling below zero, the function returns `False`.

Example use cases are provided in the `if __name__ == "__main__":` block, demonstrating how to use the `below_zero` function with different lists of operations.