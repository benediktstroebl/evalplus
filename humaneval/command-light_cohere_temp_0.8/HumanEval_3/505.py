Here's the provided Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    operations.sort()
   
    unbalanced_operations = sorted([op for op in operations if op < 0])
    return unbalanced_operations is not []
```
This function, below_zero, takes a list of operations as input and returns a boolean value indicating whether the account balance falls below zero at any point in the operations. The function sorts the operations to ensure the first operations that will remove the account balance from being zero are performed, and then checks if there are any operations remaining that are negative, which would remove the balance from being zero.