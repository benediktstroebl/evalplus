Here is a self-contained Python script that defines a function `below_zero` that solves the problem you provided: 
```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
This script defines a function `below_zero` that takes a list of integers `operations` as an argument. 

It initializes a balance to 0 and then iterates through the list of operations. When the balance falls below zero, it returns `True`. Otherwise, it returns `False`. 

Please feel free to use this solution in your markdown code block.