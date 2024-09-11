```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:
        balance += operation  # Apply each operation to the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    return False  # Return False if the balance never falls below zero


# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```
This Python script defines a function `below_zero` that takes a list of operations and returns `True` as soon as the balance falls below zero. If the balance never falls below zero, it returns `False`. The script then demonstrates the function with the provided example usage.