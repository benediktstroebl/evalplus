```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

This script defines a function `below_zero` that takes in a list of `operations` (each operation representing a deposit or withdrawal of a certain amount of money) on a bank account. The function iterates through each operation, accumulating the balance, and returns `True` immediately once the balance falls below zero, and `False` otherwise.

Here's an example usage:
```python
>>> below_zero([1, 2, -4, 5])
True
>>> below_zero([1, 2, 3])
False
```