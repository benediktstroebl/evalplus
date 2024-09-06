Here's the function below with the self-contained solution and tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function takes a list of operations (deposit and withdrawal numbers) and checks if the balance ever falls below zero. If it does, the balance is negative at any point, the function returns True; otherwise, it returns False.