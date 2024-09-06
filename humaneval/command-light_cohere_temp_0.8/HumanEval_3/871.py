```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This function checks if the account balance goes below zero during the execution of a given list of operations.