```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0: balance += operation
        elif operation < 0: balance -= operation
    return balance < 0
``` 
This script defines a function called `below_zero` that takes a list of integers `operations` as input. It uses a to maintain a balance of zero, and for every operation, it checks if the operation is positive or negative. If the balance becomes below zero, it returns `True`, otherwise, it returns `False`.