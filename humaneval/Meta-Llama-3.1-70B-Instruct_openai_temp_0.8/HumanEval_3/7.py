```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero at any point 
    given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit (positive) and withdrawal (negative) operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False


# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # Expected output: False
    print(below_zero([1, 2, -4, 5]))  # Expected output: True
```

This script initializes a balance variable to zero and iterates over the list of operations. It adds each operation to the balance and checks if the balance falls below zero. If the balance falls below zero, it immediately returns `True`. If it iterates over all operations without the balance falling below zero, it returns `False`. The test cases are included to verify the function's correctness.