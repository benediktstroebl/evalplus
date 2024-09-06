Here's the corrected Python script:
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
The function below_zero takes a list of operations as input and initializes a balance variable to 0. It then iterates over each operation in the list and checks if the balance falls below 0. If so, the function returns True, indicating the balance fell below zero. If not, it returns False, indicating no such.

The above function can be used to check for withdrawals and deposits that would cause the balance to fall below zero.