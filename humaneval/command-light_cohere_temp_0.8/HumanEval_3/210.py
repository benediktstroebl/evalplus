```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [-1, 2, 3]
    >>> below_zero(operations)
    False
    >>> operations = [0, 1, 2, 3]
    >>> below_zero(operations)
    False
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    # Use a stack (LIFO) to keep track of the operations
    stack = []
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        stack.append(operation)
        balance += operation
        else:
            while stack and balance < 0:
                balance -= stack.pop()
                stack.return stack.
    return False
 region:
        return False
    ```