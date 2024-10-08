```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of a bank account falls below zero.
    
    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.
        
    Returns:
    bool: True if the balance of account falls below zero at any point, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # Expected output: False
print(below_zero([1, 2, -4, 5]))  # Expected output: True
```