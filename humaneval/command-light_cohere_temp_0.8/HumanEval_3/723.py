Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    
    >>> operations = [1,2,-4,5]
    >>> below_zero(operations)
    True
    >>> below_zero([1,2,3])
    False
    >>> below_zero([4,5,6])
    False
    >>> below_zero([0,1,2])
    True
    """
    operations.index = 0
    balance = 0
    for i,num in enumerate(operations):
        if num < 0:
            balance -= num
        elif balance < 0:
            return True
        balance += num
    return False
```