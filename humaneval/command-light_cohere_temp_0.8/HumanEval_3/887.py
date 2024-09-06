```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
``` 
This script contains a self-contained function called `below_zero` that solves the problem of detecting if the balance of a bank account falls below zero, given a list of operations that affect the balance. 

The function uses a loop to iterate through each operation in the list, and adds each operation to the balance. If at any point the  the balance of the account becomes less than zero, the function returns `True`, indicating that the balance fell below zero.  If if the value is positive, the function will continue iterating, and will return `False` if the balance ever reaches a value greater than zero.