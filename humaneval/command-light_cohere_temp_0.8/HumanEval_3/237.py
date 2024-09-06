Here's the self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
The function uses a loop to iterate over each operation in the list, and if the balance falls below zero, the function returns True. If the balance doesn't fall below zero, the function returns False.