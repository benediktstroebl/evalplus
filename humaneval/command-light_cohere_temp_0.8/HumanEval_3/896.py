```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
        if balance < 0:
            return True
    return False
``` 
The function checks each operation's effect on the balance, and returns True if the balance falls below zero at any point, False otherwise.