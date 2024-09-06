Here's a self-contained Python script with a function that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
```
This function below_zero takes a list of operations as input. It iterates through operations from the balance starting at 0, and at each iteration, it adds the current operation to the balance. When it detects that the balance falls below zero, it returns True. Otherwise, it returns False.