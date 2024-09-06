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
This code defines a function called below_zero that takes a list of operations as input. It initializes a detects if the balance of the account falls below zero, and if so, it returns True. Otherwise, it returns False.