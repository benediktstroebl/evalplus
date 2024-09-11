```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if a bank account's balance falls below zero 
    after a series of deposit and withdrawal operations.

    Args:
    operations (List[int]): A list of integers representing deposit 
                             and withdrawal operations. Positive values 
                             represent deposits and negative values 
                             represent withdrawals.

    Returns:
    bool: True if the account balance falls below zero at any point, 
          False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Test cases
print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
print(below_zero([-1, 2, 3]))  # True
print(below_zero([10, -5, 5, -15]))  # True
```

In this script, we initialize the `balance` variable to 0 and then iterate through each operation in the `operations` list. We add the operation to the balance and check if it falls below 0. If it does, we immediately return `True`. If we finish iterating through all operations without the balance falling below 0, we return `False`.