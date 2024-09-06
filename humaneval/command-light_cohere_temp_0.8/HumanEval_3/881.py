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
This code defines a function called below_zero, which takes a list of operations as an argument. The function iterates through each operation in the list and checks if the current balance becomes negative. If it does, the function returns True. If the balance does not become negative, the function returns False.