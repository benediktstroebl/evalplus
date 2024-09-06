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
The function uses a loop to iterate through the operations list. The function performs the negative operation on the balance and returns True if the balance falls below zero. If the balance remains above or balance after the loop completes, the function will return False.