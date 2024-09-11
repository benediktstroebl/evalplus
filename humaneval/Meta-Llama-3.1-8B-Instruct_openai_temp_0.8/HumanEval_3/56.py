```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero given a list of 
    deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True as soon as the balance falls below zero
    return False  # Return False if the balance does not fall below zero


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # Expected output: False
    print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script defines a function `below_zero` that takes a list of operations as input and returns `True` if the balance falls below zero at any point, and `False` otherwise. It uses a simple iterative approach to update the balance and check if it falls below zero. The test cases are included to demonstrate the functionality of the function.