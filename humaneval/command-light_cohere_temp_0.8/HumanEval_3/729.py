```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
``` 
The above code defines a function `below_zero` that takes a list of operations as input and returns a boolean indicating whether at any point the balance of the account falls below zero. 

The function initializes a balance to zero and then iterates through each operation in the list. If the balance becomes negative during any iteration, it means the balance fell below zero, so the function returns True. Otherwise, it returns False.