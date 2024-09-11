```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point 
    after a series of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations. 
                                Positive numbers represent deposits and negative numbers represent withdrawals.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """

    # Initialize the balance to zero
    balance = 0

    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the operation amount
        balance += operation
        
        # If the balance falls below zero, return True
        if balance < 0:
            return True

    # If the function hasn't returned True after all operations, the balance never fell below zero
    return False


# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([10, -5, -7, 1]))  # True
print(below_zero([5, 10, 20]))  # False
```