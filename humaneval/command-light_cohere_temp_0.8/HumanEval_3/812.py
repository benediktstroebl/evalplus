Here's the solution:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
The function takes a list of operations, where each element is an integer that represents a deposit or withdrawal operation. The function iterates over each operation, and at the same time, it reduces the balance by the value of the operation. 

It checks if the balance falls below zero. If it does, it returns `True`. Otherwise, it returns `False`. 

This function is self-contained and solves the problem without depending on any other functions or modules.