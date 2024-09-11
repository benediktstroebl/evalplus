**Below Zero Balance Detector**
================================

A Python script to detect if a bank account's balance ever falls below zero based on a list of operations.

```python
from typing import List
from functools import reduce

def below_zero(operations: List[int]) -> bool:
    """
    Detects if a bank account's balance ever falls below zero based on a list of operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero, False otherwise.
    """
    
    # Use the reduce function to apply a lambda function cumulatively to the items of the operations list
    balance = reduce(lambda balance, operation: balance + operation, operations, 0)
    
    # Return True if the final balance is below zero, False otherwise
    return balance < 0

# Test cases
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # False
    print(below_zero([1, 2, -4, 5]))  # True
```

In this script, we use the `reduce` function from the `functools` module to cumulatively apply a lambda function to the items of the `operations` list. The lambda function takes the current balance and the next operation, adds the operation to the balance, and returns the new balance. The initial balance is set to 0.

Finally, we return `True` if the final balance is below zero and `False` otherwise.