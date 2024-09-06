Here is a self-contained Python script with a function that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
The function checks if the balance of the account ever falls below zero, and returns True. Otherwise, it returns False.