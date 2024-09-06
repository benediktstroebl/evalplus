```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
#Test the function
# [1, 2, -4, 5]
#print(below_zero([1, 2, -4, 5])) # True
``` 
The function `below_zero` accepts a list of operations and starts with a balance of 0. If the balance falls below zero, it will return `True`, otherwise, it will return `False`.  The function goes through each operation in the list and, if the balance goes below zero, it will return `True`, otherwise it will return `False`.