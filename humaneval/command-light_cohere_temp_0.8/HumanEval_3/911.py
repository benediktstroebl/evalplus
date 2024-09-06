Here is a Python script that includes the function below_zero, which is self-contained and solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```
This function takes a list of operations, where each operation is either a deposit or a withdrawal, as input. It initializes a balance to zero and iterates over each operation in the list. If it reaches a balance becomes negative, the function immediately returns True. Otherwise, it subtracts the operation from the balance and returns False if the balance falls below zero, True otherwise.