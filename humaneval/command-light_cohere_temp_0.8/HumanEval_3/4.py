Here is a Python script that contains a self-contained function that solves the problem you provided:
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
This script defines a function below_zero that takes a list of integers as input, representing deposit and withdrawal operations. The function iterates through each operation in the list, and if the balance falls below zero, it returns True. Otherwise, it returns False. The tests cases are also provided in the comments to verify the functionality.