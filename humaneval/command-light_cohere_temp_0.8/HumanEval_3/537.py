Here's the self-contained Python script with a function that solves the problem of checking if the balance of a bank account ever falls below zero, as described in your prompt:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
```

This script defines a function `below_zero` that takes a list of operations as input. The function initializes a balance of the account to 0 and then iterates through each operation in the list. If at any time the ole balance goes negative, it will decrement the balance, which will eventually cause the balance to go below zero.