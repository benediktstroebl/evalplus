Here's the Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function iterates through a list of deposit and withdrawal operations, keeping track of the current balance. It returns True if the above loop completes and the balance falls below zero.