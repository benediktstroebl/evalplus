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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function iterates through each operation in the list, updating the balance as if each operation were executed independently. If at any point the balance falls below zero, it indicates that the account balance went into a negative state at some point, and the function returns `True`. If the balance remains non-negative throughout all operations, it returns `False`. 

This solution relies on the intrinsic nature of a sum to update a value based on added values, and subtraction to update a value based on subtracted values.