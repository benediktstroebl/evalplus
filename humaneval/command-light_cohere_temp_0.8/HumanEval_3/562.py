```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        elif balance < 0:
            return True
    return False
```
This Python script defines a function below_zero that takes a list of integers as input and checks whether the balance of a bank account starts with zero and eventually falls below zero during the execution of the deposit and withdrawal operations. It iterates a value of balance to zero, and for every operation, it checks if the operation is negative, in which case it will subtract the operation from the balance, if it is not, it will check whether the balance is below zero and return True.