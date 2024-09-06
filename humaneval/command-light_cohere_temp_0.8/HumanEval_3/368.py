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
The function takes a list of operations, loops through each operation, and if the balance of the account ever falls below zero, the function will return True. Otherwise, it will return False.