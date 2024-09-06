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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It calculates the net balance of the operations and returns `True` if the balance falls below zero at any point, indicating a withdrawal exceeding deposits. Otherwise, it returns `False`.

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This function handles the problem as described in the prompt, where it starts with a zero balance and accumulates the effect of each operation. If at any point the balance becomes negative, it returns `True`, otherwise, it returns `False`.