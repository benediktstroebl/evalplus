Here's the self-contained Python script that solves the problem you described:

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False
```

This script defines a function below_zero that takes a list of operations (deposit and withdrawal) as input and detects if the balance of the account ever falls below zero. It iterates through balance variable, starting with 0, and then it loops through each operation in the list. If the operation is positive, it adds the operation to the balance, if the operation is negative, it returns True since the balance is below zero.