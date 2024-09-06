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
This function uses a loop to iterate through a list of operations, where each operation is a withdrawal from the balance. It maintains a balance at the balance by adding each operation, and it checks if the balance ever falls below zero, and if so, it returns True. If the balance remains positive after all operations, the function returns False.