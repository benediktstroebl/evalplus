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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It simulates the actions on the account by updating the balance accordingly. Then it checks if the balance ever falls below zero, and returns `True` if it does, and `False` otherwise. 

Here is an example usage:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This example aligns with the given problem statement and outputs `False` for the first case and `True` for the second case.