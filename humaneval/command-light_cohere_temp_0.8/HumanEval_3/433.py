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
This function takes a list of operations, including deposits and withdrawals, as input. It iterates through loop, where it adds operations to the balance, and if the balance ever falls below zero, it returns True; otherwise, it returns False.