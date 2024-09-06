```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
``` 
The function takes a list of operations, then iterates through each operation. It sets the balance to zero and checks if the balance falls below zero. If so, it returns True. If the balance is greater than or equal to zero, the function will return False.