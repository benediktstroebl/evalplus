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

The code defines a function `below_zero` that takes a list of `operations` as an argument. It iterates through each operation in the list and accumulates them into a variable called `balance`. If at any point the `balance` falls below zero, it immediately returns `True`. If all operations add up to a non-negative balance, it returns `False` at the end.

This solution adheres to the given test cases and will return `False` for lists like `[1, 2, 3]` and `True` for lists like `[1, 2, -4, 5]`.