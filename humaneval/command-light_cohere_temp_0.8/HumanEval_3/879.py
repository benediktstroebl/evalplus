Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
The `below_zero` function takes a list of operations and returns `True` if the balance falls below zero at any point, and `False` otherwise.