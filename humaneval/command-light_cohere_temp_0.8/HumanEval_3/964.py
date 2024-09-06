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
This script defines a function below_zero that takes a list of operations, iterates through the list, and returns True if at any point the balance falls below zero, and False otherwise. The script also passes the