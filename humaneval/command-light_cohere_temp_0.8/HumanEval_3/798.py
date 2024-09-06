Here's a self-contained Python script that solves the problem you described: 

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
``` 

This script defines a function `below_zero` that takes a list of operations and checks if any of them would cause the balance of the account to go below zero.  It uses a the `balance` variable to keep track of the account balance, and iterates through the list of operations.