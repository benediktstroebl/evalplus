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

The `below_zero` function iterates through the list of operations, accumulating a balance, and returns `True` if the balance ever falls below zero, otherwise, it returns `False`. 

Here's an example usage illustration:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
``` 
This example usage demonstrates the function's behavior, specifically detecting the scenario where the balance falls below zero.