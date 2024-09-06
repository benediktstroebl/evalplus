```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False
``` 
This script defines a function below_zero that takes a list of operations as input. It then iterates through operations and maintains the balance. The function returns True if at any point the balance falls below zero, and False otherwise.