```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
``` 
This script defines a function called below_zero that takes a list of operations (deposit and withdrawal) as input. The function loops through each operation and adds it to the balance, if the balance becomes negative it returns True, otherwise it returns False. 
It uses the typing module for better type checking.