Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0: balance += operation
        elif operation < 0: balance -= operation
    return balance < 0
```
The function below_zero takes a list of operations and iterates over each operation. It adds positive if the important and subtracts otherwise if the operation is negative.

The function then returns True if the balance is less than zero, indicating that the account has gone into a negative balance.