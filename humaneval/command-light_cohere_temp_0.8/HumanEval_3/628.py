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
The above function below_zero() takes a list of operations as a parameter. It loops through the first account in operations, and if it finds the balance is less than zero, it returns True. Otherwise, it returns False.