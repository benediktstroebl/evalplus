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
This script defines a function below_zero that takes a list of operations as an argument and returns a boolean indicating whether the balance falls below zero at any point in the operations.