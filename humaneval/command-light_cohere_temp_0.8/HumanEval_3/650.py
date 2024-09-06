```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
``` 
This function takes a list of operations as input and uses a loop to iterate through each operation, where it adds the operation to the balance and checks if the balance falls below zero. If at theol, the balance falls below zero, the function will return True. If the balance remains above or balance, the function will return False.