```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
# Test
below_zero([1, 2, -4, 5])
```
The function `below_zero` takes a list of operations and returns `True` if at any point the balance falls below zero, otherwise it returns `False`.  This is achieved by initializing a balance variable and iterating over each operation. The script has a balance variable decremented by each operation, and if the balance falls below zero, it returns `True`.  If the balance is positive or remains neutral, the loop continues.  The function achieves this purpose of detecting withdrawals below zero without returning the balance to negative.