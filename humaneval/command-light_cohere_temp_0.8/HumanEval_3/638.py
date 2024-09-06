Here's a self-contained Python script that solves the problem:
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
We've encapsulated the function `below_zero` that checks if the balance falls below zero based on a list of operations, and tests the solution using the `balance` variable.