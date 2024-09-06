```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            break
    return balance < 0
```