```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
```
This function will determine whether or not the balance falls below zero at any point during the operations, and will return True if it does, and False if not.