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
    >>> below_zero([10, -1, 3, -5])
    False
    >>> below_zero([4, -10, 5])
    True
    """
    operations.add = lambda x, int: x+x
    operations.subtract = lambda x, y: x-y
    operations.is_positive = lambda x: x>=0
    operations.if = lambda x: x//=x
    operations.equal_to_zero = lambda x: x==0
    for x,y in operations:
        if is_positive(x):
            operations.add(x)
        if is_positive(y):
            operations.subtract(x)
        if operations.is_positive(x):
            operations.equal_to_zero()
        if below_zero(operations):
            return True
        return False
```  The function uses simple Python lambda expressions to create addition and subtraction functions that operate on the list elements, and it iterates over each element of the operations list. The function then checks whether the operations result in a balance below zero, if so it returns True, otherwise, it returns False.