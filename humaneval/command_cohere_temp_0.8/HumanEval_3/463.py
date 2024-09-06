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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the net balance of the bank account after each operation. If the balance ever falls below zero, it returns `True`, otherwise, it returns `False`. The function works correctly as described in the provided test cases.