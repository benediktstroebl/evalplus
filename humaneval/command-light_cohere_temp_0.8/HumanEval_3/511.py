Here's a self-contained Python script that defines a function `below_zero` to solve the problem:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```

You can use this `below_zero` function in your markdown code block to solve the problem and determine if the balance falls below zero.