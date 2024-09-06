Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```

This script provides a function called `below_zero` that accepts a list of integers, operations, as input. The function first initializes a balance of the account to zero, then iterates over the list of operations. Once the balance falls below zero, the function returns `True`. Otherwise, it continues iterating and returns `False`.