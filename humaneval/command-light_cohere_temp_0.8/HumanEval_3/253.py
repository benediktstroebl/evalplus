Here's the solution:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```

This function takes a list of operations and iterates through them, incrementing the balance variable. It returns `True` if the balance falls below zero and thus, the account balance becomes negative.  The function is self-contained and does not require any external variables or functions to solve the problem.