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
The function uses a loop to iterate through the operations and checks if the balance ever falls below zero. The function then returns True if the balance ever becomes negative and False if not.