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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the balance as if each operation were executed independently. If at any point the balance falls below zero, it indicates that the account balance became negative at some point, and the function returns `True`. If the balance never falls below zero after processing all operations, it returns `False`. 

This solution follows the prompt's expectations, as it returns `True` for the input `[1, 2, -4, 5]` and `False` for the input `[1, 2, 3]`.