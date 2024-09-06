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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It simulates the operations on the account and returns `True` if at any point the balance falls below zero, and `False` otherwise. The function updates the balance after each operation and checks if it becomes negative at any point.