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

The `below_zero` function iterates through the list of operations, accumulating a balance by adding each operation. If at any point the balance falls below zero, it immediately returns `True`. If the loop completes without the balance dropping below zero, it returns `False`. This solution follows the structured approach of looping through the operations and maintaining a running balance.