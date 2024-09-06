```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
``` 
This function takes a list of operations (deposit and withdrawal) as input and iterates over each operation in the list. It starts with an initial balance of 0 and checks if the balance ever falls below 0. If it reaches a this point, it returns True, otherwise, it returns False.