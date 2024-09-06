Here's the provided Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    """
   
    balance of the account is represented by a float variable balance, which is 
    initially set to zero.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([0, 2, 3])
    False
    >>> below_zero([4, 0, 3])
    True
    >>> below_zero([100, -100, 200])
    False
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
The provided function checks if the account balance ever falls below zero. It iterates through operations and adds the operations to the balance. The function returns True if any operation would make the balance go below zero, otherwise it returns False.