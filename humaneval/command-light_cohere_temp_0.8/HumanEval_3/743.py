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
This script defines a function called `below_zero` that takes a list of integers `operations` as input. It initializes a test if the balance of the account starts with zero. The loop iterates through the operations and keeps track of the balance. If at any point the would balance go below zero, it returns `True`. Otherwise, it returns `False`. The test code passes this function and prints the result.