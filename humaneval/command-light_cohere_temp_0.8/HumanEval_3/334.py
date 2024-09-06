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
This function will test the operations to see if the balance ever falls below zero and returns True, otherwise, it will return False.