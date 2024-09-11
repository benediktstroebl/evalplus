```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if at any point the balance of the account falls below zero.
    
    Args:
        operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
        bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # If it does, return True
    return False  # If no operation makes the balance fall below zero, return False

# Example use cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([1, -2, 3, -4]))  # True
print(below_zero([10, 20, 30]))  # False
```