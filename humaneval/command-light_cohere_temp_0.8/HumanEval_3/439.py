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
The function `below_zero` takes a list of operations, loops through each operation and uses a balance variable to keep track of the account balance. The function first checks if the balance falls below zero, and if so, it returns `True`. Otherwise, it returns `False`.