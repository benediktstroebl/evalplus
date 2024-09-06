Here's a Python script that defines a self-contained function that solves the problem you provided:
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

This function performs the same logic as your provided function. It iterates through operations, and if the balance ever falls below zero, it returns True. If the balance stays positive, the function returns False.