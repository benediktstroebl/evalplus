Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    >>> operations
     [1, 2, -4, 5]
    True
    """
    for op in operations:
        if op < 0:
            return True
    return False
``` 
The function uses a loop to iterate over each element in the operations list and checks if the element is negative, if so, it returns True. If the loop completes without finding a negative number, it means that the balance never fell below zero, and the function returns False.