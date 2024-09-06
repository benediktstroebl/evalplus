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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the balance by adding the effect of each operation. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went below zero at some point. If the balance never falls below zero after processing all operations, it returns `False`.

The function is designed to efficiently handle the problem statement in O(n), where n is the number of operations, as it performs a single pass through the input list of operations.