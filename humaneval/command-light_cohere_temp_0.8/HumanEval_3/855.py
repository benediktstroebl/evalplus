Here is the self-contained Python script with a function that solves the problem:
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

This function takes a list of operations as input, and it iterates over each operation. If the balance falls below zero, it returns True. Otherwise, it returns False. The function uses the necessary variables and it calculates the balance at the end of iteration and returns the result.