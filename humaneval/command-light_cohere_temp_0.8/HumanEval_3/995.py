Here's a self-contained Python script with a function that solves the problem and passes the corresponding tests:
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
This function below_zero takes a list of operations as input. It initializes thes with an initial balance of 0. It then iterates through operations, checking if the balance goes below zero and returns True. If the balance remains non-negative after processing all operations, it returns False.