```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
``` 
This function takes a list of operations, adds them all up, and then checks if the balance is less than zero. It will return `True` if the balance is less than zero, and `False` otherwise.