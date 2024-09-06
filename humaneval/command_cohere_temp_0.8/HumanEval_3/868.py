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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the running balance by adding the `op`. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went negative at some point. If none of the operations cause the balance to go negative, it returns `False` at the end. 

This solution is efficient because it uses a single pass to iterate through the operations list, so it has a time complexity of O(n), where 'n' is the length of the operations list.