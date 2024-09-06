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

The script defines a function `below_zero` that takes a list of operations on a bank account and returns `True` if the balance of the account ever falls below zero, and `False` otherwise. The function iterates through the list of operations, updating the account balance after each operation. If at any point the balance falls below zero, the function returns `True`. If the balance remains non-negative until the end of the operation list, the function returns `False`. 

This solution follows the prompt's expected functionality, where the function returns `True` for the input `[1, 2, -4, 5]` and `False` for the input `[1, 2, 3]`.