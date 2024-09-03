```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if account balance falls below zero at any point.
    Returns True if it does, False otherwise.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```