Here's the provided Python script with the self-contained function `below_zero` that solves the problem:
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

This function takes a list of deposit and withdrawal operations and iterates through them. It starts with an initial balance of 0 and checks if at any point, the balance goes below zero. If the condition is met, it returns `True`; otherwise, it returns `False`.

This self-contained function can be used to solve the problem and pass corresponding tests.