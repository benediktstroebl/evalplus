```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account's balance falls below zero given a list of deposit and withdrawal operations.
    
    Args:
        operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.
        
    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # If it is, return True immediately
    return False  # If we've iterated over all operations without going below zero, return False


# Example use cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([-1, -2, -3]))  # True
    print(below_zero([]))  # False
```