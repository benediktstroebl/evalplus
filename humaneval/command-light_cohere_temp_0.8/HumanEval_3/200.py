Here is the self-contained Python script with a function that solves the problem:
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
This script defines a function below_zero that takes a list of operations (deposit and withdrawal) as an argument. It initializes a first variable balance with 0 and then iterates through each operation, checking if the balance ever falls below 0. If so happens true, the function returns True. If the balance remains above 0 after all operations, the function would return False.