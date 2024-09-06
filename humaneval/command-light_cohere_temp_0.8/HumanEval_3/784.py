```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([6, -1, 3])
    False
    >>> below_zero([0, 1, -3, 4])
    True
    """
    operations.count_with_zero = 0
    for num in operations:
        if num < 0:
            return True
        operations.count_with_zero += 1
    if count_with_zero >= 2:
        return True
    return False
```  This script defines a function that checks if a list of operations will cause the account balance to go below zero. The function keeps track of the number of operations that will cause a negative balance and returns True if this count is greater than or equal to 2.