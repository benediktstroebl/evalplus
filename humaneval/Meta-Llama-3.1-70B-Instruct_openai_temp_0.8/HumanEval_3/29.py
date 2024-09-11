```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account ever falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
    
    Returns:
    bool: True if the balance falls below zero at any point, False otherwise.
    """
    
    # Initialize the balance to zero
    balance = 0
    
    # Iterate over each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation
        balance += operation
        
        # Check if the balance is below zero
        if balance < 0:
            # If the balance is below zero, return True immediately
            return True
    
    # If we've iterated over all operations and the balance is never below zero, return False
    return False


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([10, -5, -3, -2]))  # True
    print(below_zero([-1, 2, 3]))  # True
    print(below_zero([0, 0, 0]))  # False
```