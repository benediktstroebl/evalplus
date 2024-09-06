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

The `below_zero` function iterates through the list of `operations`, summing them to the current `balance`. It returns `True` if the balance ever falls below zero, and `False` otherwise. This algorithm has a time complexity of `O(n)` since it checks each operation in the list once.