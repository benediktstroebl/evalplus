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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the running balance of the bank account after each operation. If at any point the balance falls below zero, the function returns `True`. Otherwise, it returns `False`. The function is tested against the provided test cases and is expected to pass.