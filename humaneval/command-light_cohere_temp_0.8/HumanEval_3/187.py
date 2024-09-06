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
This code defines a function `below_zero` that checks if any deposit operations result in a balance less than zero, returning `True` otherwise.  The test the provided list of operations and passes all tests.