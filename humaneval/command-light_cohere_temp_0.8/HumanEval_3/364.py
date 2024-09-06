Here's a self-contained Python script with a function below_zero that solves the problem you described: 

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

This script defines a function below_zero that takes a list of integers as an argument, representing deposit and withdrawal operations for a bank account. It initializes the fact variable balance to 0, and then iterates over the list of operations. If at any point the occurrence of a deposit or withdrawal operation that would cause the balance to go below 0, the function returns True. Otherwise, it continues the process and returns False.