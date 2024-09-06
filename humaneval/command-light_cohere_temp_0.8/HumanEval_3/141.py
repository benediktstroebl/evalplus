```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
``` 
This function, `below_zero`, takes a list of integers `operations` as an argument. It initializes a value of `balance` variable to 0. Then, it iterates over each `operation` in the list, if the current `balance` is less than 0, it returns `True`. Otherwise, it returns `False`. 

You can test this function by passing the list of operations as an argument to see if the balance falls below zero at any point.