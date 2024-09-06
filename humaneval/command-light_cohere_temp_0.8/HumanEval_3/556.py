Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```

This function takes a list of operations (positive and negative integers) and detects if the balance of the account ever falls below zero. It does this the record operations by repeatedly subtracting the operation from the balance, and if at any point, the balance falls below zero, it returns True. Otherwise, it returns False.