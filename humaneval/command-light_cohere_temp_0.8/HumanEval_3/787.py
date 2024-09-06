Here's the solution to the problem:

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

This code takes a list of operations (deposit and/or withdrawal from the account) as an argument. It iterates through operations and checks if the balance ever falls below zero. If it does, it returns True, indicating that the balance is below zero. Otherwise, it returns False. 

Note: The code assumes that all operations are valid integers, and does not perform any type checking or error handling. It is a most simple implementation of the problem.