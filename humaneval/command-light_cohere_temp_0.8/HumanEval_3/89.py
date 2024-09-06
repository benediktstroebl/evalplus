Here's the updated code:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False
```
The function `below_zero` takes a list of integers, `operations`, as input. It iterates over each operations and checks whether the balance of the account starts to go below zero. If this happens, the function returns `True`. Otherwise, it returns `False`.