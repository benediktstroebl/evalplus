Here's a self-contained Python function that solves the problem:
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
The function iterates through a list of deposit and withdrawal operations, keeping track of the balance after each operation. The function returns True if the balance falls below zero at any point in the loop, indicating that the account balance has gone below zero. Otherwise, the function returns False.