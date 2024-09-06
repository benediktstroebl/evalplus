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
This code defines a function `below_zero` that takes a list of operations as an argument. It initializes a goal balance at zero. Then, it iterates through each operation and if the balance falls below zero, the function returns `True`. Otherwise, it will return `False`.  The function will help to identify and return the operation that will cause the balance to go below zero.