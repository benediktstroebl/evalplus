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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the running balance by adding the `op`. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went negative at some point. If no such scenario is encountered, it returns `False` at the end. 

This solution is efficient and linear, O(n), in terms of time complexity since it iterates through each operation once, and has a constant O(1) space complexity.