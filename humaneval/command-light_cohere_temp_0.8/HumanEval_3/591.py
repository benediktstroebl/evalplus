Here is a Python script with a self-contained function that solves the problem and passes the tests:
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

The function uses a loop to iterate through the operations, and adds each operation to the balance. If the balance falls below zero, the function returns True, otherwise, it returns False.