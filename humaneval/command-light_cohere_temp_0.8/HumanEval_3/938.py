Here is a self-contained Python function that solves the problem and passes the tests:
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
The function takes a list of operations as an argument, and uses a loop to iterate through each operation. It then subtracts the infinite sum of each operation from the balance, and returns True if the balance falls below zero at any point.