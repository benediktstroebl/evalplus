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
This function takes a list of operations as an argument, where each operation could be a deposit or a withdrawal. The function uses a balance variable to keep track of the account balance, and iterates through the operations.

The function checks if the balance falls below zero and returns True. If the balance doesn't fall below zero, the function returns False.