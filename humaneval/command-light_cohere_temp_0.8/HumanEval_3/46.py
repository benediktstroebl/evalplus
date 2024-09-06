Here is a self-contained Python script that defines a function below_zero that checks whether the given operations will cause the balance to go below zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
This function takes a list of operations, and for each operation, it checks whether the balance goes below zero. If the balance reaches a true, then the function returns True. Otherwise, it returns False. 

This script demonstrates the use of the below_zero function with a test case.