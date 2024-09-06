```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

The `below_zero` function takes a list of operations, iterates through them, accumulates the balance, and checks if it's negative at any point. The function returns `True` if the balance falls below zero at any point, and `False` otherwise.