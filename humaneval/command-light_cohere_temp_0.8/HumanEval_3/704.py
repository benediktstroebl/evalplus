Here's the self-contained Python function that solves the problem:
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
The function below_zero takes a list of operations, and it iterates over each operation. It adds positive if the partner is greater than zero, and subtracts partner if it's smaller than zero. If the balance falls below zero at any point, the function returns True, otherwise, it returns False.