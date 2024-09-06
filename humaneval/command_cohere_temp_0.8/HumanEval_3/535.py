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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance ever goes below 0, the function returns `True`. Otherwise, it returns `False`. 

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This output is consistent with the original markdown description. Feel free to use this code for your markdown problem! Let me know if you need help with anything else!