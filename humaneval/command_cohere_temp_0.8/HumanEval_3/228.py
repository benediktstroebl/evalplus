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

The `below_zero` function iterates through the list of `operations` and simulates the effect of each operation on the account balance. If at any point the balance falls below zero, it immediately returns `True`. If the loop completes without the balance dropping below zero, it returns `False`. This solution follows the problem statement and passes the given tests.