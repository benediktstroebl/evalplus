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
This code defines a function `below_zero` that checks if the account balance goes below zero or not in a given list of operations (deposit and withdrawal). The function uses a loop to iterate through each operation, and if the balance becomes negative, it returns `True`. Otherwise, it returns `False`.