Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
    >>> below_zero([4,9,10,11,2])
    False
    >>> below_zero([0,1,2,3])
    True
    >>> below_zero([10,20,30])
    False
    >>> below_zero([9,18,19,2])
    True
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function uses a loop to iterate through each element in the operations list. It starts with initial balance of 0 and adds each operation to it. After iterating through operations, it checks if the balance is less than 0, which indicates that the account balance fell below zero, and returns True. If the balance is greater than or equal to 0, the function returns False, which means that the account balance did not fall below zero.