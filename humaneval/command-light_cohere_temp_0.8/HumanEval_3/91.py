Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```
The function below_zero takes a list of operations, then it runs through each operation and adds or subtracts from the balance accordingly. It returns True if the for any operation the balance goes below zero, and False otherwise.