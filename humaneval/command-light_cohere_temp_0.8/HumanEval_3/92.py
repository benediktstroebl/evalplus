Here's a self-contained Python script with a function that solves the problem you described:
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
This function takes a list of operations and iterates through them. For each operation, if the balance of the account goes below zero, the function returns True, indicating that the account balance fell below zero. Otherwise, it continues iterating through the next operation, and if the balance becomes non-negative, the function returns False, indicating that the balance did not fall below zero.