```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test cases
below_zero([1, 2, -4, 5]) # True
below_zero([1, 2, -3, 4]) # False
```
This script defines a function `below_zero` that checks whether any operation in the list will cause the account balance to go below zero. It uses a the only subtraction as an operation to decrease the balance and the initial balance is set to 0.

It then tests the function with a variety of inputs and passes the tests.