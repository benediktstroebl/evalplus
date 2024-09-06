Here is a self-contained Python script that defines a function below_zero that solves the problem you provided:
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
The function takes a list of operations as input and uses a loop to iterate over each operation. The function then checks if the balance falls below zero. If the balance falls below zero, the function returns True. If the balance is greater than or equal to zero, the function returns False.