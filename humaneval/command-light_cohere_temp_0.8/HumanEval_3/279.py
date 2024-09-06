```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
The function checks whether any of the operations will cause the balance to go below zero. It iterates through the balance by keeping track of the sum of all operations, and at the end of the loop, it checks whether this balance is less than zero.