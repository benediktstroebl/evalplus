```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False
``` 
This function uses a loop to iterate through the operations, adds the operations if it's a deposit, and checks if the balance goes below zero, and if it is, returns True, otherwise, returns False.