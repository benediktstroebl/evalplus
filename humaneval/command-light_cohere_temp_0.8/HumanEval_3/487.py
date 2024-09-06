Here is a self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
The function below_zero takes a list of operations as input, where each operation is either a deposit or a withdrawal from the account. It then iterates through operations and keeps track of the balance of the account. The function will return True if the balance falls below zero, and False otherwise.