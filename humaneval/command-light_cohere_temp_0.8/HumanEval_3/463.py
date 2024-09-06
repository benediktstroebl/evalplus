Here is a Python script with a self-contained function that solves the problem:
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

This script defines a function called `below_zero` that takes a list of operations, and it checks whether the balance falls below zero at any point. It uses a balance variable to keep track of the balance, and for each operation, if the balance becomes negative, it returns True. Otherwise, it returns False.