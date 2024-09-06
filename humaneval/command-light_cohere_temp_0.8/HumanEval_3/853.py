Here's the self-contained Python function that solves the problem you described:

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
```

You can use this function with a list of operations to check if the balance falls below zero.  The test cases are provided.