Here's a self-contained Python script that defines a function below_zero, which solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```

This function takes a list of operations as input and iterates over the list. It maintains a balance of the account by adding deposits and subtracting withdrawals. The function returns True if at any point the balance falls below zero, and False otherwise.