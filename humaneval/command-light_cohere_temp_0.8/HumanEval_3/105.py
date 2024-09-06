```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 1, -3, 2])
    False
    >>> below_zero([5, -4, 3, 1])
    True
    """

    # Define a counter
    balance = 0
    operations_count = len(operations)

    # Loop through the operations list
    for i in range(operations_count):
        # Check if the operation is a withdrawal or deposit
        if operations[i] > 0:  # Assuming only positive operations are deposits
            balance += operations[i]
        elif operations[i] < 0:
            return True  # If balance falls below zero, return True

    return False  # If no conditions are met, return False


# Test cases
# Test with a series of operations, some of which are negative and others are positive
# Test with operations that start with zero balance

```