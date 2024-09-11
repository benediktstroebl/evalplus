```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # initialize balance to zero
    for operation in operations:
        balance += operation  # update balance with each operation
        if balance < 0:  # check if balance falls below zero
            return True  # return True if balance falls below zero
    return False  # return False if no operation causes balance to fall below zero


# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It iterates over each operation in the list, updates the balance accordingly, and checks if the balance falls below zero after each operation. If it does, the function immediately returns `True`. If no operation causes the balance to fall below zero, the function returns `False` after checking all operations. The test cases demonstrate the function's behavior with different input lists.