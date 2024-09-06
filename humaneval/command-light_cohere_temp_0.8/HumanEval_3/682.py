Here's the code to solve the problem:
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
The above function iterates over the operations list, where each element is either a deposit or a withdrawal. It adds up the This particular element to the balance and checks if the balance falls below 0, in which case it returns True, otherwise, it returns False.