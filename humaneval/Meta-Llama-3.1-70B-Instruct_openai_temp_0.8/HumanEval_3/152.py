```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point 
    given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of integers representing deposit and withdrawal operations.
                                Positive values represent deposits and negative values represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is less than zero
            return True  # If the balance is less than zero, return True
    return False  # If the function hasn't returned True, the balance never fell below zero, so return False

# Example use cases:
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we initialize the balance to zero and then iterate over each operation in the list, updating the balance at each step. If the balance ever falls below zero, we immediately return True. If we make it through the entire list without the balance falling below zero, we return False.