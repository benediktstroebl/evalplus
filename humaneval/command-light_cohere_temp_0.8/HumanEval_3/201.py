```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
        if balance < 0:
            return True
    return False
``` 
This Python function below_zero takes a list of operations as input. It iterates through operations to calculate the balance of an account and returns True if at any point the balance falls below zero. Otherwise, it returns False.