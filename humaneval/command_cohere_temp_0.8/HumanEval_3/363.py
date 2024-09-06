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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the running balance by adding the `op`. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went below zero at some point. If none of the operations cause the balance to go below zero, it returns `False` at the end. 

This solution is concise and efficiently solves the problem using basic Python syntax and logic.