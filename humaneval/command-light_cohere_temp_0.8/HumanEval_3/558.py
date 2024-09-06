Here's the self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
This function takes a list of operations (deposit and withdrawal) and iterates over the operations, checking if the balance ever falls below zero. If it does, it returns `True`. Otherwise, it returns `False`. 

This is a simple, self-contained way to solve the problem.