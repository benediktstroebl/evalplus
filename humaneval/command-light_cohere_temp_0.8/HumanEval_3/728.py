```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
We've defined a function called below_zero, which takes a list of integers as an argument. The function starts with an empty balance variable and then iterates over the list of operations. During each iteration, it checks if the current balance is less than zero, and if so, it returns True. If the balance doesn't go below zero, it will return False after the loop completes.