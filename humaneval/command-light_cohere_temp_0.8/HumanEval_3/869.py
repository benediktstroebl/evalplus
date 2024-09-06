```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
The function `below_zero` takes a list of operations, adds them up, and checks if the balance fell below zero.  The end result is `True` if the balance ever becomes less than zero, and `False` otherwise.