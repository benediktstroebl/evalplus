```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False."""
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Example use cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
    print(below_zero([1, -2, 3, -4]))  # True
    print(below_zero([1, 2, 3, 4]))  # False
```

This Python script defines the function `below_zero` which iterates through each operation in the list. If at any point the balance falls below zero, it immediately returns `True`. If it iterates through all operations without the balance falling below zero, it returns `False`. Example use cases are provided to demonstrate its functionality.