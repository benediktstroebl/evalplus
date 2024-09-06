```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0, 1, 2]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    for num in operations:
        if num < 0:
            return True
    return False
```  The code defines a function `below_zero` that takes a list of operations as input. The function iterates over each operation in the list and checks if the operation is negative. If a operation is negative, the function returns True, indicating that the account balance has fallen below zero. If the operation is not negative, the function returns False. 

This function follows the approach of iterating over the operations and checking if any operation is negative.