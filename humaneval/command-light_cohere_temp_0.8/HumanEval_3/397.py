```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
# Example usage
below_zero([1, 2, -4, 5]) #This will return True
```
The function checks the operations against the balance of an account, starting from zero. If the balance ever falls below zero, the function returns True, otherwise, it returns False. 

This function is self-contained and can be used to solve the problem and pass the test without requiring external functions or variables.