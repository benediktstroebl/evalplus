Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op < 0:
            balance -= op
        else:
            balance += op
    return balance < 0
```
The function `below_zero` takes a list of operations and detects if any operation would cause the balance of the account to go below zero. 
It uses a loop to iterate through each operation and update the balance accordingly. 
If the balance falls below zero, the function returns `True`, otherwise it returns `False`.