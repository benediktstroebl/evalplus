Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:

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
The provided Python function below_zero, takes a list of operations as input. It iterates through operations one by one and keeps adding the operation to the balance. After the iteration, it checks if the balance is below zero, and if so, it returns True. Otherwise, it returns False.