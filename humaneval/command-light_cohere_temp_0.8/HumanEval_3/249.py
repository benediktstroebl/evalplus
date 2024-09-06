```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:  # deposit, it will increase the balance
            balance += operation
        elif operation < 0:  # withdrawal, it will decrease the balance
            balance -= operation
    return balance < 0
```
This script defines a function `below_zero` that takes a list of operations, and iterates through them. During each iteration, it adds positive operations to the balance and subtracts negative operations from the balance. The function returns `True` if the balance falls below zero, and `False` otherwise.