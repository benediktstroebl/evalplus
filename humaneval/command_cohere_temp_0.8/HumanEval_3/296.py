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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). The function iterates through each operation in the list, updating the balance by adding the `op`. If the balance ever falls below 0 at any point, it immediately returns `True`, indicating that the account balance went below zero at least once. If no such instance is encountered, it returns `False` at the end of processing all operations, assuming the account balance never went below zero. 

This solution is efficient, with a time complexity of O(n), where 'n' is the number of operations in the input list.