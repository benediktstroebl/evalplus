Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```
The function takes a list of operations, loops through the operations and adds each one to the balance, if the balance falls below zero, the function will return True. If the balance is not below zero, the function will return False.