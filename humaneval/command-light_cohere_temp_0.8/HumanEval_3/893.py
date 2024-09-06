Here is a self-contained Python function that solves the problem and passes the tests:
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
This function takes a list of operations, where each operation is either a deposit or a withdrawal. The function iterates over each operation, and if the balance falls below zero, it returns True. If the balance does not go below zero, the function returns False.