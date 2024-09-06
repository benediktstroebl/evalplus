```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
            return True
    return False
``` 
This function uses a loop to iterate through a list of operations, and adds each operation to the balance. The function returns True if the balance falls below zero, otherwise returns False.