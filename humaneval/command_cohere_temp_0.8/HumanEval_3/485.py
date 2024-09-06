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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It calculates the balance by summing up the operations, then determines whether the balance falls below zero at any point. If it does, the function returns `True`, otherwise it returns `False`.

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This function fulfills the requirement of the problem statement and aligns with the given tests. It handles the scenario of tracking the balance and determining if it falls below zero at any moment.