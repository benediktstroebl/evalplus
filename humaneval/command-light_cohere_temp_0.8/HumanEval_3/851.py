Here's a self-contained Python function that solves the problem:
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
The function uses a loop to iterate through the list of operations. It adds the balance for each operation (deposit or withdrawal) and if the balance falls below zero, the function returns True. If the loop completes without the balance ever becoming negative, the function will return False, indicating that the balance never fell below zero.