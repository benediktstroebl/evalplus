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
This function takes a list of operations, which are integers that represent deposit and withdrawal operations, and it returns True if the balance of the account goes below zero at any point in the loop, and False otherwise.