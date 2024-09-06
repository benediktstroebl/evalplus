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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance ever falls below 0, the function returns `True`. Otherwise, it returns `False`. The script passes the given tests of returning `False` for the first test of `([1, 2, 3])` and returning `True` for the second test of `([1, 2, -4, 5])`.