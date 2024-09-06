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

The code defines a function `below_zero` that takes a list of `operations` as an argument. It iterates through each operation in the list and calculates the running balance of the bank account. If the balance falls below zero at any point, the function immediately returns `True`. If the balance remains non-negative until the end of the list, it returns `False`. This functionality is exemplified in the docstring already, which showcases the function's behavior for two distinct sample-input lists.