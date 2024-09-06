```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1,2,3])
    False
    >>> below_zero([1,2,3,4])
    False
    >>> below_zero([1,2,-3,4])
    True
    >>> below_zero([10,10,10])
    False
    >>> below_zero([100,100,100])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    if balance < 0:
        return True
    else:
        return False
```  The function uses a loop to iterate over the operations list and adds each operation to the balance. The if the balance goes below zero, it returns True. Otherwise, it returns False.