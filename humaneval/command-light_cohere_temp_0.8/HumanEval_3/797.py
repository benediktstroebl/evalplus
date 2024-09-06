Here's the provided Python script with a self-contained function that solves the problem of detecting if the balance of the account ever falls below zero:
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
The `below_zero` function takes a list of integers as input and initializes a balance variable to zero. It then iterates over each operations and uses a `while` loop to detect if the balance ever falls below zero and returns `True` accordingly. If the balance does not fall below zero, the loop exits, and the function returns `False`.