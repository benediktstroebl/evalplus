Here's the code for a self-contained function that solves the problem:
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
This code defines a function below_zero that takes a list of integers as an input. It iterates through operations, checking if the balance ever falls below zero. If it does, the function returns True, indicating that the account balance fell below zero at some point. Otherwise, it returns False, which means that the balance never became negative.