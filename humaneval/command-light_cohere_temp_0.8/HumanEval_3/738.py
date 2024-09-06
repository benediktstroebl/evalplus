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
This script defines a function below_zero that takes a list of operations and checks if the balance of the account goes below zero at any point in the list of operations.