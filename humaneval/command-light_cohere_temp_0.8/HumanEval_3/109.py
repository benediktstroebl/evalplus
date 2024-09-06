Here is a self-contained Python script that solves the problem of checking if the balance of a bank account ever falls below zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
```

This function takes a list of operations, where each operation is either a deposit or a withdrawal from the account. It initializes theal balance to zero, and then iterates through the operations, subtracting the amount of each operation from the balance.

The function returns True if at any point the balance falls below zero, and False otherwise.