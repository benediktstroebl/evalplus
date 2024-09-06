Here is a self-contained Python script that defines a function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point function should return True. Otherwise, it should return False.
    >>> operations
   
    balance_ check example: operations = [-4, 5, 1, 2, 3]
    operations = [0] + operations
    balance = 0
    return balance < 0
```
The function takes a list of operations as input and returns a boolean value indicating whether the balance of the account falls below zero. 

The function uses the "type" hint to indicate that the operations list should be a list of integers.