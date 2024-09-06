Here's a self-contained Python script with a function that solves the problem:
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
This script defines a function `below_zero` that takes a list of integers as an argument. It initializes a for each operation in the list, it will check if the balance falls below zero. It then iterates through operations and checks if the balance becomes negative. If it does, the function will return `True`, indicating that the balance fell below zero. Otherwise, it will return `False`.