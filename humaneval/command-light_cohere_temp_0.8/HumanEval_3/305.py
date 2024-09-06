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
This function takes a list of operations and iterates over each operation. It compares the one by one. It checks if the balance falls below zero. If it does, the function returns True. Otherwise, it returns False.