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
    >>> below_zero([5, -1, -3])
    False
    >>> below_zero([100, -200, -300])
    True
    >>> below_zero([-500, -300, -200])
    False
    >>> below_zero([-1000, 0, -500])
    True
    """
    operations.sort()
   
    balance = 0
    for num in operations:
        if num < 0 and balance < 0:
            return True
        elif num < 0:
            balance -= num
        else:
            balance += num
    return balance >= 0
``` 
This script defines a function `below_zero` that takes a list of operations as an argument. It sorts the the this list and iterates through each number in the list. Finally, it checks if the balance is less than zero, and returns `True` if this condition is met. If not, it returns `False`.