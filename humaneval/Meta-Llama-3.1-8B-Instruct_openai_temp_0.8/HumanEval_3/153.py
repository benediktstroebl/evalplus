Here is a self-contained Python script that solves the problem in a markdown code block:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance by adding the current operation
        
        if balance < 0:  # Check if the balance has fallen below zero
            return True  # If it has, return True immediately
    
    return False  # If we've iterated over the entire list without returning True, the balance never fell below zero

# Example usage:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. The function iterates over each operation in the list, updating the balance accordingly, and returns `True` as soon as the balance falls below zero. If the function iterates over the entire list without returning `True`, it returns `False`.