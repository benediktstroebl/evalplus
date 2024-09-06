```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function checks if the balance falls below zero and returns `True` if it does, and `False` otherwise.  The balance is represented as an integer list, and is passed to the function through the `operations` parameter.