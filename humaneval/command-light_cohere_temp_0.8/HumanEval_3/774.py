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
This code defines a function below_zero that takes a list of operations, iterates through the list, and for every operation, it checks if the balance goes below zero. It returns True if the reasons, and False otherwise.