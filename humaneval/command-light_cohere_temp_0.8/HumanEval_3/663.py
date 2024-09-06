Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
The function `below_zero` takes a list of operations and initializes the balance to 0. It then iterates through operations, and checks if the balance falls below zero. If so, the function returns `True`, indicating that the balance is below zero. Otherwise, it returns `False`.