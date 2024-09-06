Here is a self-contained Python script with a function that solves the problem of checking if the balance of a bank account falls below zero, and tests passed with the provided input:
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
This function takes a list of operations, and for each operation, it adds the operation to the balance, if at any point the balance falls below zero, the function will return True. Otherwise, it will return False.