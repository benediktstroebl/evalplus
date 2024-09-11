```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account with initial zero balance falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation in the list
        balance += operation  # Apply the operation to the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    return False  # If the function hasn't returned True, the balance never fell below zero


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([-1, 2, 3]))  # True
    print(below_zero([1, 1, 1]))  # False
```