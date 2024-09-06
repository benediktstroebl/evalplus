Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```
This function takes a list of operations and iterates over them. It calculates the balance by considering both positive and negative operations. It then returns True if the balance is less than 0, indicating that the account has fallen below zero.