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
This function takes a list of operations (deposit and withdrawal numbers) as an argument. It initializes a balanced with 0, and then iterates over each operation. If the balance falls below zero, it returns True. Otherwise, it returns False.