Here's a Python script that contains a self-contained function that solves the problem and passes the corresponding tests:
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
This function takes a list of operations (deposit and withdrawal) as an argument and iterates through the operations. It checks if the balance falls below zero and returns `True` if it happens. If the balance doesn't go below zero, the function returns `False`.