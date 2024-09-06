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
The function checks if the balance of the account falls below zero. If so, the balance becomes negative, the function returns True, and otherwise, it returns False.