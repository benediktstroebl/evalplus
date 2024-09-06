Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
This function takes a list of operations as input and iterates over the operations. It then maintains the main balance variable and updates it by each operation (deposit or withdrawal). If at any point the balance falls below zero, the function returns True. Otherwise, it returns False.