Here's the code that solves the problem:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            balance += operation
    return balance < 0
```

This code defines a function below_zero that takes a list of operations as an argument and returns a boolean value. It iterates through through operations and maintains the balance, checking if the balance ever falls below zero to return True, and if it's greater than zero, it returns False.