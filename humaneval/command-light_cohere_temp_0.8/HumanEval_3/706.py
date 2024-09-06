Here's the self-contained Python script with the `below_zero` function:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
```
This script defines a function called `below_zero` that takes a list of integers as input and returns a boolean value. It simulates a operation of deposits and withdrawals from an account, starting from an initial balance of 0, to check if the balance falls below zero.