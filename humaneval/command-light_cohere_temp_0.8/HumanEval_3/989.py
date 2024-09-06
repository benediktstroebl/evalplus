Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            balance += operation
    return balance < 0
```
This function takes a list of operations and iterates over them, checking if any operation would make the balance go below zero. The function returns True if the balance is less than zero, and False otherwise.