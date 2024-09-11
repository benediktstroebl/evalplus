```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of an account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Apply the operation to the balance
        balance += operation
        
        # Check if the balance has fallen below zero
        if balance < 0:
            # If it has, return True immediately
            return True
    
    # If we've iterated over all operations and the balance hasn't fallen below zero, return False
    return False


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([10, -5, -7]))  # True
    print(below_zero([-1, 2, 3]))  # True
    print(below_zero([0, 0, 0]))  # False
```