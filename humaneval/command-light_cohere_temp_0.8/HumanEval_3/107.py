Here's a self-contained Python script that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False
```
This function takes a list of operations (deposit and withdrawal) as input and uses a loop to iterate through the operations. It keeps track of the balance and if at any point the balance falls below zero, the function returns True, indicating that the account balance has gone below zero. Otherwise, it returns False, indicating that the balance has remained positive throughout the operations.